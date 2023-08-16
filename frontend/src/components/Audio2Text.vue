<template>
  <div>
    <navigation-bar></navigation-bar>
    <div>
      <el-card>
        <el-upload
            class="el-upload"
            drag
            :limit="1"
            action="http://127.0.0.1:8000/api/audio2text/audioupload/"
            :on-success="uploadSuccess"
            :on-error="uploadError"
            :on-exceed="uploadExceed"
        >
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
          <div slot="tip" class="el-upload__tip">只能上传mp3、m4a、wav文件</div>
        </el-upload>
      </el-card>

      <el-card>
        <el-input
            type="textarea"
            :rows="15"
            v-model="trans_res"
        ></el-input>
      </el-card>

      <el-card>
        <el-row :gutter="20">
          <el-col :span="8"><button  class="button-setting" v-on:click="startTransfer">开始转换</button></el-col>
          <el-col :span="8"><button  class="button-setting" v-on:click="downloadFile">下载文件</button></el-col>
          <el-col :span="8"><button  class="button-setting" v-on:click="skip2Text2Audio">文字转录音</button></el-col>
        </el-row>
      </el-card>
    </div>
  </div>
</template>

<script>
import NavigationBar from "@/components/static/NavigationBar";
export default {
  name: "Audio2Text",
  components: {
    NavigationBar
  },
  data () {
    return {
      trans_res: ''
    }
  },
  methods: {
    // 上传接口调用成功，code为100
    uploadSuccess(res) {
      console.log(res)
      if (res.code === 100) {
        this.$notify.success({
          title: '成功',
          message: '文件上传成功!'
        })
      } else {
        this.uploadError()
      }
    },

    // 文件上传失败
    uploadError() {
      this.$notify.error({
        title: '错误',
        message: '文件上传失败！'
      })
    },

    // 文件个数超过限制
    uploadExceed() {
      this.$notify.warning({
        title: '错误',
        message: '您已经添加了一个文件，如需替换，请删除已添加的多余文件！'
      })
    },

    // 开始转换
    startTransfer() {
      let _this = this
      this.$http.request({
        url: _this.$url + 'api/audio2text/audio2text/',
        method: 'GET'
      }).then(function (response) {
        if (response.data.code === 100) {
          _this.trans_res = response.data.text
        } else {
          this.$notify.error({
            title: '失败',
            message: response.data.msg
          })
        }
      })
    },

    // 下载文件
    downloadFile() {

    },

    // 跳到文字转语音
    skip2Text2Audio() {

    }
  }
}
</script>

<style scoped>
.button-setting {
  padding: 0 24px;
  border: 1px solid #009B62;
  font-size: 15px;
  color: #FFFFFF;
  line-height: 50px;
  border-radius: 4px;
  cursor: pointer;
  background-color: #009B62;
}

</style>