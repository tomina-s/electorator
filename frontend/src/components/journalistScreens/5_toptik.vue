<template>
  <div class="block">
    <div class="container-fluid" :style="{'background-color': 'transparent !important'}">

      <div class="row row_block text-white display-2 font-weight-bold">
        <div class ="col-12 text-center pt-5">
          {{data.num_tik}}

        </div>
      </div>
      <div class="row row_block text-white display-3 font-weight-bold">
        <div class="col-12 text-center">
          {{data.population}}

        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "5_toptik",
  props: {
    data: {
      num_tik: String,
      population: Number
    }
  },
  data() {
    console.log("toptik", this.data)
      return {
      }
  }
}

</script>

<style scoped>
.block {

    height: 100vh;

    background-image:url("../../assets/journalistScreens/5.png");

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