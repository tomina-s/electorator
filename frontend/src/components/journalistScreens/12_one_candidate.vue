<template>
  <div class="block">
  <div class="container-fluid text-white align-self-start mr-0">
    <div class="row">
        <div class="col-7 display-4 text-right  pt-2 mt-5" v-for="(el, i) in one_candidate.slice(0,1)" :key="i">

              <div class="col display-4 font-weight-bold">
                {{el.name}}
              </div >
          <br>
              <div class="col">
                {{el.birthday}} г.р.
              </div>
              <div class="col">
                {{el.party}}
              </div>
              <div class="col h2">
                <br>
                <p>
                Место рождения:
                <br>
              {{el.birthday_place}}
                <br>
                </p>
              </div>
              <div class="col h2">
                <p>

                Образование:
                <br>
                {{el.education}}
                <br>
                </p>
              </div>
              <div class="col h2">
                <p>
                Основное место работы:
                <br>
                {{el.work}}
                <br>
                </p>

              </div>
          <br>
          <br>
          <br>
         <div class="row align-items-end mt-5">
      <div class="col-1 display-2 text-right align-self-end mt-5" v-for="(el, i) in one_candidate.slice(0,1)" :key="i">
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
  height: 100vh;
  width: 72.5vh;
}

</style>