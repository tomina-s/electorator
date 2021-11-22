<template>
  <div class="block">
  <div class="container-fluid text-white align-self-start">
    <div class="row">
        <div class="col-7 h1 text-right  pt-2 mt-5" v-for="(el, i) in one_candidate.slice(0,1)" :key="i">

              <div class="col h1 font-weight-bold">
                {{el.name}}
              </div >
          <br>
              <div class="col">
                {{el.birthday}} г.р.
              </div>
              <div class="col">
                {{el.party}}
              </div>
              <div class="col h3">
                <p>
                Место рождения:
                <br>
              {{el.birthday_place}}
                <br>
                </p>
              </div>
              <div class="col h3">
                <p>

                Образование:
                <br>
                {{el.education}}
                <br>
                </p>
              </div>
              <div class="col h3">
                <p>
                Основное место работы:
                <br>
                {{el.work}}
                <br>
                </p>

              </div>
          <br>

         <div class="row mt-2">
      <div class="col-1 display-4 text-right align-self-end mt-5" v-for="(el, i) in one_candidate.slice(0,1)" :key="i">
              <div class="col-1 text-left font-weight-bold">
                <p>
              {{el.sum_votes}}%
                  <br>
                </p>
              </div>
      </div>
    </div>
        </div>
      <div class="col-5" v-for="(el, i) in one_candidate.slice(0,1)" :key="i">
        <img class="photo" :src="el.photo"/>
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
    background-size: 100% auto;

    display: flex;
    align-items: center;
   justify-content: center;
}
.photo{
  height: 99vh;
  width: 71vh;
}

</style>