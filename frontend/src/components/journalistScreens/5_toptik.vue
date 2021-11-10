<template>
  <div>
    {{data.population}}
    {{data.num_tik}}
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
    console.log("toptik", this.data)
      return {
      }
  }
}

</script>

<style scoped>

</style>