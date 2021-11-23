<template>
<div class ="block">
    <div class="container-fluid align-items-end mt-5">
    <div class="row justify-content-center " v-for="(pair, i) in candidates" :key="i">
      <div class="col-2" v-for="(can, j) in pair" :key="j">
        <div  class="text-white text-center h5">
          <div class="d-flex justify-content-center img-fluid">
            <div class="rounded-circle wrap_avatar">
              <img class="ans_avatar" :src="can.photo">
            </div>
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


.block {

    height: 100vh;
    background-image:url("../../assets/journalistScreens/2.png");
    background-size: 100% auto;

    display: flex;
    align-items: center;
    justify-content: center;
}
.ans_avatar {
    width: 15vh; /*180px;*/
}
.wrap_avatar {
    position: relative;
    height: 15vh; /*180px;*/
    width: 15vh;/*170px;*/
    overflow: hidden;
}
</style>