from django.shortcuts import render




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
    return ret