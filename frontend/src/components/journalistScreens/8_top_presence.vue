<template>
  <div class="block">
    <div class="container-fluid" :style="{'background-color': 'transparent !important'}">

      <div class="row row_block text-white display-3 font-weight-bold">
        <div class ="col-12 text-center mt-5 pt-5">
          {{data.num_tik}}

        </div>
      </div>
      <div class="row row_block text-white display-3 font-weight-bold">
        <div class="col-12 text-center mt-5 pt-5">
          {{data.presence}}%
        </div>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  name: "8_top_presence",
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
.block {

    height: 100vh;

    background-image:url("../../assets/journalistScreens/8.png");
    background-size: 100% auto;

    display: flex;
    align-items: center;
    justify-content: center;
}
.row_block{
  border:5px #1b1e21;
  height: 50vh;
  display: flex;
  align-items: center;
  justify-content: center;

}

</style>


