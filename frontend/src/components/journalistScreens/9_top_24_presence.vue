<template>
  <div class ="block">
    <div class="container-fluid mt-5 text-white text-center font-weight-bold display-4" :style="{'background-color': 'transparent !important'}">
     <div class="row_block_25">
     </div>
      <div class="row row_block_25">
       <div class="col-12" v-for="(el, i) in top24.slice(0,3)" :key="i">
         {{el.num_tik}}
       </div>
     </div>
      <div class="row row_block">
        <div class ="col-12">
          {{top24[3].min_presence}}% избирателей
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "9_top_24_presence",
  props: {
    data: []


  },
  data() {
    console.log("top24presence", this.data)
      return {
      top24: this.data
      }
  }
}
</script>

<style scoped>
.block {

    height: 100vh;

    background-image:url("../../assets/journalistScreens/9.png");
    background-size: 100% auto;

    display: flex;
    align-items: center;
    justify-content: center;
}
.row_block{

  height: 45vh;
  display: flex;
  align-items: center;
  justify-content: center;

}
.row_block_25{

  height: 24vh;
  display: flex;
  align-items: center;
  justify-content: center;

}
</style>