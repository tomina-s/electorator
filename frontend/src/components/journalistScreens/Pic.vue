<template>
  <div class="rounded-circle d-flex ans_avatar justify-content-center img-fluid">
    <img :src="src"/>
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
    height: 15vh; /*180px;*/
    width: 15vh;/*170px;*/
    overflow: hidden;
}
</style>