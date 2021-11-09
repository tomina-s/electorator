<template>
  <div class="container">
    <li  v-for="item in items" :key="item.num_tik,item.presence">
       {{data.}}


    </li>

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