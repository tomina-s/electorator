<template>
  <div>
    <img :src="`${require('../../assets/logo_shadow.png')}`"
         :style="{
          'height': '100vh'
    }">
    <p :style="{
        'position': 'fixed',
        'width': '25%',
        'color': '#FFFFFF',
        'font-size': '96px',
        'font-weight': 'bold',
        'text-align': 'center',
        'top': '25%',
        'left': '62%'
      }"
    >
      {{ data.open_uik }} открыто
    </p>
    <br/>
    <p :style="{
        'position': 'fixed',
        'width': '25%',
        'color': '#FFFFFF',
        'font-size': '96px',
        'font-weight': 'bold',
        'text-align': 'center',
        'top': '60%',
        'left': '62%'
      }">
      {{ data.population }} избирателей
    </p>
  </div>
</template>

<script>
export default {
  name: "1_opened",
  props: {
    data: {
      open_uik: Number,
      population: Number
    }
  },
  data() {
    console.log(this.data)
      return {
      }
  }
}
</script>

<style scoped>

</style>