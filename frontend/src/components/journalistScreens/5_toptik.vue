<template>
  <div class="bg-image"
       :style="{
          'background-image': `url(${require('../../assets/journalistScreens/5.png')})`,
          'height': '100vh'
        }"
  >
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
      {{ data.num_tik }}
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
      {{ data.population }}
    </p>
  </div>
</template>

<script>
export default {
  name: "5_toptik",
  props: {
    data: {
      num_tik: String,
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