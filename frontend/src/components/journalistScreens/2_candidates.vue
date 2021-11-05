<template>
  <div class="container">
    <div class="row" v-for="(pair, i) in candidates" :key="i">
      <div class="col-sm" v-for="(can, j) in pair" :key="j">
        <div  class="">
          <img class="ans_avatar rounded-circle" :src="can.photo"/>
          <br>
          <p>{{can.party}}</p>
          <br>
          <p>{{ can.name }}</p>
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
    height: 90px;
    width: 90px;
}

</style>