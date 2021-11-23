<template>
<div class ="block">
    <div class="container-fluid align-items-end mt-3">
    <div class="row justify-content-center " v-for="(pair, i) in candidates" :key="i">
      <div class="col-2" v-for="(can, j) in pair" :key="j">
        <div  class="text-white text-center h5">
          <pic :src="can.photo"/>
            <br>
          <div class="font-weight-bold">
            {{can.name}}
          </div>
          <div class="font-weight-light">
            {{can.party}}
          </div>
          <br>
        </div>
      </div>
    </div>
  </div>
  </div>
</template>
<script>
import pic from './Pic'
export default {
  name: "2_candidates",
  components: {
    pic
  },
  props: {
    data: []
  },
  data() {
    return {
      candidates: this.data.slice().splice(0,2)
    }
  }
}
</script>

<style scoped>
.block {

    height: 100vh;
    background-image:url("../../assets/journalistScreens/2.png");
    background-size: 100% auto;

    display: flex;
    align-items: center;
    justify-content: center;
}
</style>