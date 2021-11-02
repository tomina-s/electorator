<template>
  <div class="bg-image"
       :style="{
          'background-image': `url(${require('../../assets/journalistScreens/1.png')})`,
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
      {{ data.opened }}
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
      {{ data.voters }}
    </p>
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