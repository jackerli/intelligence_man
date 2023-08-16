from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse

import os

audio_save_path = "D:\\Desktop\\intelligence_man\\intelligence_man\\audio2text\\audios"

# upload audio file
def audioupload(request):
    """
    audio file upload
    code: 100 or 101. 100: upload successfully  101: upload error
    """
    ret = {'code': 100, 'msg': None}
    if request.method == "POST":
        # 获取上传的文件，如果没有，就默认为None
        my_file = request.FILES.get("file", None)

        if not my_file:
            ret['code'] = 101
            ret['msg'] = '录音文件不存在'
            return ret

        f = open(os.path.join(audio_save_path, my_file.name), "wb+")
        # 分块写入文件
        for chunk in my_file.chunks():
            f.write(chunk)
        f.close()
    else:
        ret['code'] = 101
        ret['msg'] = '录音文件上传失败'

    return JsonResponse(ret)


# delete audio file
def audiodelete(request):
    """
    delete files of audio directory
    code: 100 or 101. 100: delete successfully  101: delete error
    """
    ret = {'code': 100, 'msg': None}

    del_list = os.listdir(audio_save_path)
    try:
        for f in del_list:
            file_path = os.path.join(file_path, f)
            os.remove(file_path)
    except Exception as e:
        ret['code'] = 100
        ret['msg'] = '删除录音文件失败'

    return JsonResponse(ret)


# transfer audio to text
def audio2text(filename):
    """
    code: 100 or 101. 100: transfer successfully  101: transfer something error
    """
    ret = {'code': 100, 'msg': None, 'text': None, 'sentences': None}

    # transfer other format to wav
    prefix = filename.split('.')[0]
    suffix = filename.split('.')[1]

    if suffix == 'm4a':
        command = f"ffmpeg -i {0}.m4a -acodec pcm_s16le -ac 2 -ar 44100 {1}.wav".format(prefix, prefix)
        os.system(command)
    elif suffix == 'mp3':
        command = f"fmpeg -loglevel quiet -y -i {0} -ar 16000 -ac 1 {1}.wav".format(prefix, prefix)
        os.system(command)

    filename_new = prefix + '.wav'

    # audio2text api
    try:
        inference_pipeline = pipeline(
            task=Tasks.auto_speech_recognition,
            model='damo/speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-pytorch',
            model_revision="v1.2.4")
        rec_result = inference_pipeline(audio_in=filename_new)
        ret['text'] = rec_result['text']
        ret['sentences'] = rec_result['sentences']
    except Exception as e:
        ret['code'] = 101
        ret['msg'] = e

    ret['msg'] = 'transfer successfully'

    # return audio text
    return JsonResponse(ret)