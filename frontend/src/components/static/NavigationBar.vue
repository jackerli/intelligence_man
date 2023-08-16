<template>
  <div>
    <el-menu mode="horizontal"
             background-color="#009B62"
             text-color="#fff"
             active-text-color="#FFFFFF"
             style="top: 0;">
      <el-menu-item index="1"><a v-on:click="skip2Audio2Text">录音转文字</a></el-menu-item>
      <el-menu-item index="2"><a v-on:click="skip2Text2Audio">文字转语音</a></el-menu-item>
      <el-menu-item index="3"><a v-on:click="skip2AIReply">智能问答</a></el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: "NavigationBar",
  data() {
    return {}
  },
  methods: {
    skip2Audio2Text: function () {
      let _this = this
      _this.$router.push({path: '/audio2text'})
    },
    skip2Text2Audio: function () {
      let _this = this
      _this.$router.push({path: '/text2audio'})
    },
    skip2AIReply: function () {
      let _this = this
      _this.$router.push({path: '/aireply'})
    }
  }
}
</script>

<style scoped>

</style>