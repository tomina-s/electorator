<template>
  <div class ="block align-items-center">
    <div class="container-fluid mt-5 pt-5">
      <div class ="row justify-content-center text-white h5">
        <div class = "col-5 ml-5 pl-5" v-for="(elem, i) in candidates" :key="i">
          <div class="row mt-md-4 align-middle" v-for="(el, j) in elem" :key="j">

            <div class="rounded-circle wrap_avatar">
              <img class="ans_avatar" :src="el.photo">
            </div>

            <div class="col font-weight-bold text-left">
              {{el.name}}
              <div class="row font-weight-light pl-3">
                  {{el.party}}
              </div>
            </div>

            <div class="col  font-weight-bold text-center h3">
              {{el.sum_votes}}%
            </div>

          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: "17_votes",
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
}
.ans_avatar {
    width: 14vh; /*180px;*/
}
.wrap_avatar {
    position: relative;
    height: 14vh;/*150px*/
    width: 14vh;/*140px*/
    overflow: hidden;
}
.block {
  height: 100vh;
  background-image: url("../../assets/journalistScreens/17_1.png");
  background-size: 100% auto;
  display: flex;
  align-items: center;
  justify-content: center;
}

</style>