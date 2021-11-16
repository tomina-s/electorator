<template>
<div class ="block">
    <div class="container-fluid align-items-end">
    <div class="row justify-content-center " v-for="(pair, i) in candidates" :key="i">
      <div class="col-2" v-for="(can, j) in pair" :key="j">
        <div  class="text-white text-center h3">
          <div class="d-flex justify-content-center img-fluid">
          <img class="ans_avatar rounded-circle" :src="can.photo"/>
          </div>
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
export default {
  name: "2_candidates",
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
.ans_avatar {
    height: 180px;
    width: 170px;
}
.block {

    height: 100vh;
    background-image:url("../../assets/journalistScreens/2.png");
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>