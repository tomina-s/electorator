<template>
  <div


  >
    votes_presence
    {{data.percent_votes}}
    {{data.presence}}

  </div>
</template>

<script>
export default {
  name: "11_votespresence",
  props: {
    data: {
      percent_votes: String,
      presence: String
    }
  },
  data() {
    console.log("votespresence", this.data)
      return {
      }
  }
}
</script>

<style scoped>

</style>