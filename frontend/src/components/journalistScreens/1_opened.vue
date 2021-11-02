<template>
  <div class="bg-image"
       :style="{
          'background-image': `url(${require('../../assets/journalistScreens/1.png')})`,
          'height': '100vh'
        }"
  >
    Участков открыто {{ data.opened }}
    <br/>
    Избирателей {{ data.voters }}
  </div>
</template>

<script>
export default {
  name: "1_opened",
  props: {
    data: {
      opened: Number,
      voters: Number
    }
  },
  data() {
      return {
      }
  }
}
</script>

<style scoped>

</style>