import os
from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
# Create your views here.

# transfer text to audio
def text2audio(filename, voice_sel):
    """
    code: 100 or 101 or 102. 100: transfer successfully  101: read text error  102: transfer something error
    """
    ret = {'code': 100, 'msg': None, 'file': None}

    # read text file
    input_text = ''
    try:
        f = open(filename, encoding="utf-8")
        text = f.read()
        input_text = text
        f.close()
    except Exception as e:
        ret['code'] = 101
        ret['msg'] = 'read text error'

    # read text file failed, return
    if ret['code'] != 100:
        return ret

    print(input_text)
    # text2audio api
    try:
        sambert_hifigan_tts = pipeline(task=Tasks.text_to_speech, model='damo/speech_sambert-hifigan_tts_zh-cn_16k')
        print(type(input_text))
        output = sambert_hifigan_tts(input=input_text, voice=voice_sel)
        wav = output[OutputKeys.OUTPUT_WAV]
        output_file = filename.split('.')[0] + '.wav'
        with open(output_file, 'wb') as f:
            f.write(wav)
            f.close()
    except Exception as e:
        ret['code'] = 102
        ret['msg'] = 'transfer something error'
        ret['file'] = filename.split('.')[0] + '.wav'
        print(e)

    # return audio file name
    return ret
