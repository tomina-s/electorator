<template>
  <div class="block">
    <div class="container-fluid" :style="{'background-color': 'transparent !important'}">
      <div class="row">
        <div class ="col-12 align-self-start">
        {{data.population}}
        </div>
      </div>
      <div class="row">
        <div class="col-12 align-self-end">
          {{data.num_tik}}
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

</style>