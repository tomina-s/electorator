<template>
  <div class="block">
  <div class="container-fluid text-white">
    <div class="row">
        <div class="col-7 display-1 text-right align-self-start" v-for="(el, i) in one_candidate.slice(0,1)" :key="i">
              <div class="col">
                {{el.name}}
              </div >
              <div class="col">

                {{el.birthday}}
              </div>
              <div class="col">
                {{el.party}}
              </div>
              <div class="col h1">
                Место рождения
              {{el.birthday_place}}
              </div>
              <div class="col h1">
                Образование
                {{el.education}}
              </div>
              <div class="col h1">
                Основное место работы
                {{el.work}}
              </div>
        </div>
    </div>
    <div class="row">
      <div class="col-1 display-1 text-right" v-for="(el, i) in one_candidate.slice(0,1)" :key="i">
              <div class="col-1 text-left">
              {{el.sum_votes}}%
              </div>
      </div>
    </div>

  </div>
  </div>

</template>

<script>
export default {
  name: "12_one_candidate",
  props: {
    data: []

  },
  data() {
    console.log("one_candidate", this.data)
      return {
      one_candidate:this.data
      }
  }
}
</script>

<style scoped>
.block {

    height: 100vh;

    background-image:url("../../assets/journalistScreens/12.png");

    display: flex;
    align-items: center;
   justify-content: center;
}

</style>