<template>
  <div


  >
    top_presence
    {{data.num_tik}}
    {{data.presence}}

  </div>
</template>

<script>
export default {
  name: "5_toptik",
  props: {
    data: {
      num_tik: String,
      presence: Number
    }
  },
  data() {
    console.log("toppresence", this.data)
      return {
      }
  }
}
</script>

<style scoped>

</style>