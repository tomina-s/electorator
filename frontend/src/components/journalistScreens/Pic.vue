<template>
  <div class="d-flex justify-content-center img-fluid">
    <div class="rounded-circle wrap_avatar">
      <img class="ans_avatar" :src="src">
    </div>
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
    width: 15vh; /*180px;*/
}
.wrap_avatar {
    position: relative;
    height: 15vh; /*180px;*/
    width: 15vh;/*170px;*/
    overflow: hidden;
}
</style>