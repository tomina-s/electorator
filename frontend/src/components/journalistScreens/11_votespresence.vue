<template>
  <div class="block">
    <div class="container-fluid mt-5" :style="{'background-color': 'transparent !important'}">

      <div class="row row_block text-white display-3 font-weight-bold">
        <div class ="col-12 text-center mt-5 pt-5">
          {{data.percent_votes}}

        </div>
      </div>
      <div class="row row_block text-white display-3 font-weight-bold">
        <div class="col-12 text-center mt-5 pt-5">
          {{data.presence}} избирателей

        </div>
      </div>
    </div>
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
.block {

    height: 100vh;

    background-image:url("../../assets/journalistScreens/11.png");
    background-size: 100% auto;

    display: flex;
    align-items: center;
    justify-content: center;
}
.row_block{
  border:5px #1b1e21;
  height: 45vh;
  display: flex;
  align-items: center;
  justify-content: center;

}
</style>