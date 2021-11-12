<template>
 {{data}}

</template>

<script>
export default {
  name: "4_two_candidates",
  props: {
    data: []
  },
  data() {
    console.log('two_candidates',this.data)
      return {
        candidates: this.data
      }
  }
}
</script>

<style scoped>
.block {
  border: #1b1e21;
    height: 100vh;

    background-image:url("../../assets/journalistScreens/4.png");
    display: flex;
    align-items: center;
    justify-content: center;
}
.row_block{
  border:5px #1b1e21;
  width: 100vh ;
  height: 25vh;
  display: flex;
  align-items: center;
  justify-content: center;

}

img{
    height: 300px;
    width: 300px;
    border: #1b1e21 5px;
}

</style>