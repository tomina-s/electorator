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
</style>