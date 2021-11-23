<template>
  <div class="d-flex rounded-circle wrap_avatar justify-content-center img-fluid">
    <img class="ans_avatar" :src="src"/>
  </div>
</template>

<script>
export default {
  props: {
    src: String
  },
  name: "Pic"
}
</script>

<style scoped>
.ans_avatar {
    height: 20vh; /*180px;*/
    width: 20vh;/*170px;*/
}
.wrap_avatar {
    height: 15vh; /*180px;*/
    width: 15vh;/*170px;*/
    overflow: hidden;
}
</style>