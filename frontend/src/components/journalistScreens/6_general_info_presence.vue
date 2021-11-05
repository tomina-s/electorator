<template>
  <div


  >
    general_info_presence
    {{data.open}}
    {{data.sum_electorators}}
    {{data.presence}}


  </div>
</template>

<script>
export default {
  name: "6_general_info_presence",
  props: {
    data: {
      open: Number,
      sum_electorators: Number,
      presence: String
    }
  },
  data() {
    console.log("general_info_presence", this.data)
      return {
      }
  }
}
</script>

<style scoped>

</style>