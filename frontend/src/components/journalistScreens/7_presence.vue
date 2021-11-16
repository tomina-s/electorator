<template>
<div class ="block">
  <div class="container-fluid mt-5" :style="{'background-color': 'transparent !important'}">

      <div class="row text-white h1 ml-3 mt-5">
        <div class="col-6" v-for="(elem, i) in presence" :key="i">
          <div class="row" v-for="(el, j) in elem" :key="j">
            <div class="col text-left">
              {{el.num_tik}}
            </div>
            <div class="col text-right">
              {{el.presence}}%
            </div>
          </div>
        </div>
      </div>
  </div>
</div>
</template>

<script>
export default {
  name: "7_presence",
  props: {
    data: []
  },
  data() {
      return {
        presence: this.data.slice().splice(0,2)
      }
  }
}
</script>

<style scoped>
.block {

    height: 100vh;

    background-image:url("../../assets/journalistScreens/7.png");

    display: flex;
    align-items: center;
    justify-content: center;
}

</style>