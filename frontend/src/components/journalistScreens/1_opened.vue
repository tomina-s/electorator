<template>
  <div class ="block">
    <div class="container-fluid mb-5">
      <div class="row">
        <div class="col-6">

        </div>
        <div class="col-6">
          <div class="row row_block mb-5 pb-5 display-3 text-white text-center font-weight-bold">
            <div class="col-6">
              {{data.open_uik}}
            </div>
          </div>
          <div class="row row_block display-3 mt-1 text-white text-center font-weight-bold">
            <div class="col-6">
              {{data.population}}
            </div>
          </div>



        </div>
    </div>
  </div>
 </div>
</template>

<script>
export default {
  name: "1_opened",
  props: {
    data: {
      open_uik: Number,
      population: Number
    }
  },
  data() {
    console.log(this.data)
      return {
      }
  }
}
</script>

<style scoped>
.block {

    height: 100vh;

    background-image:url("../../assets/journalistScreens/1.png");
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