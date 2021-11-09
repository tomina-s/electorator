<template>
  <div>
          <img :src="`${require('../../assets/journalistScreens/7.png')}`"
             :style="{
          'height': '100vh'
        }"
      >
    {{data}}
  </div>
</template>

<script>
export default {
  name: "7_presence",
  props: {
    data: []


  },
  data() {
    console.log("presence", this.data)
      return {
      }
  }
}
</script>

<style scoped>

</style>