<template>
  <div>
      <img :src="`${require('../../assets/logo_shadow.png')}`"
             :style="{
          'height': '100vh'
        }"
      >
      <span :style="{
            'width': '25%',
            'position': 'fixed',
            'color': '#FFFFFF',
            'font-size': '146px',
            'font-weight': 'bold',
            'top': '25%',
            'right': '15%'
          }"
        >
        Выборы<br/>Мэра<br/>Москвы
      </span>
  </div>



</template>

<script>
export default {
  name: "0_screen",
  props: {
    data: {
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