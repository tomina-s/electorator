<template>

  <div class="container">
      <div class="row">
      <div class="col-sm-6" v-for="(elem, i) in presence.slice(0,8)" :key="i">
        <div class="row" v-for="(el, j) in elem" :key="j">

        {{el.num_tik}}
        {{el.presence}}

        </div>

      </div>
       <div class="col-sm-6" v-for="(elem, i) in presence.slice(8,16)" :key="i">
        <div class="row" v-for="(el, j) in elem" :key="j">

        {{el.num_tik}}
        {{el.presence}}

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
    console.log('presence',this.data)
      return {
        presence: this.data
      }
  }
}
</script>

<style scoped>
.block {
    border: 1px solid blueviolet;
    height: 400px;
    display: flex;
    align-items: center;
    justify-content: center;


}

</style>