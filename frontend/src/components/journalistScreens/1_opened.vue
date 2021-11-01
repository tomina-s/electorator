<template>
  Участков открыто {{ data.opened }}
  <br/>
  Избирателей {{ data.voters }}
</template>

<script>
export default {
  name: "1_opened",
  props: {
    data: {
      opened: Number,
      voters: Number
    }
  }
}
</script>

<style scoped>

</style>