<template>
  <div class ="block">
    <div class="container-fluid mb-5">
      <div class="row">
        <div class="col-6">

        </div>
        <div class="col-6">
          <div class="row row_block display-3 text-white text-center font-weight-bold">
            <div class="col-6">
              {{data.open}}
            </div>
          </div>
          <div class="row row_block display-3 text-white text-center font-weight-bold">
            <div class="col-6">
              {{data.sum_electorators}}
            </div>
          </div>
          <div class="row row_block display-3 text-white text-center font-weight-bold">
            <div class="col-6">
              {{data.presence}}
            </div>
          </div>


        </div>
    </div>
  </div>
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
.block {

    height: 100vh;
    background-image:url("../../assets/journalistScreens/6.png");

    background-size: 100% auto;
    display: flex;
    align-items: center;
    justify-content: center;
}
.row_block{
  border:5px #1b1e21;
  height: 33vh;
  display: flex;
  align-items: center;
  justify-content: center;

}
</style>