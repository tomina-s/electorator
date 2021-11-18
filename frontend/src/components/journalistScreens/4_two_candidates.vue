<template>
  <div class = "block align-items-start ">
    <div class = "container-fluid text-white mt-4 pl-5 pr-5">
      <div class = "row ">
        <div class = "col-3 " v-for="(el, i) in candidates.slice(0,1)" :key="i">
          <img class="photo" :src="el.photo"/>
        </div>
        <div class = "col-3 pl-4" v-for="(el, i) in candidates.slice(0,1)" :key="i">
          <p class = "h1 font-weight-light">{{el.birthday}} г.р.</p>
          <br>
          <p class = "h2">
            Место рождения:
            <br>
            {{el.birthday_place}}</p>
          <br>
          <p class = "h2">
            Образование:
            <br>
             {{el.education}}
          </p>
          <br>
          <p class = "h2">
            Основное место работы:
            <br>
            {{el.work}}</p>
          <br>

          <br>
          <p class = "h2">
             Занимаемая должность:
            <br>
            {{el.position}}</p>
        </div>
        <div class = "col-3 text-right " v-for="(el, i) in candidates.slice(1,2)" :key="i">
          <p class = "h1 font-weight-light">{{el.birthday}} г.р.
          </p>
          <br>
         <p class = "h2">
            Место рождения:
            <br>
            {{el.birthday_place}}</p>
          <br>
          <p class = "h2">
            Образование:
            <br>
             {{el.education}}
          </p>
          <br>
          <p class = "h2">
            Основное место работы:
            <br>
            {{el.work}}</p>
          <br>

          <br>
          <p class = "h2">
             Занимаемая должность:
            <br>
            {{el.position}}</p>
        </div>
        <div class = "col-3" v-for="(el, i) in candidates.slice(1,2)" :key="i">
           <img class="photo ml=0" :src="el.photo"/>
        </div>
      </div>
      <div class="row mt-4">
          <div class="col-6 " v-for="(el, i) in candidates.slice(0,1)" :key="i">
            <p class="display-3">{{el.name}}</p>
            <p class ="h1 font-weight-bold">{{el.party}}</p>
            <p class ="h1">{{el.polit_position}}</p>
          </div>
          <div class="col-6 text-right " v-for="(el, i) in candidates.slice(1,2)" :key="i">

            <p class="display-3">{{el.name}}</p>
            <p class="h1 font-weight-bold">{{el.party}}</p>
            <p class = "h1">{{el.polit_position}}</p>

          </div>
        </div>
    </div>
  </div>
 </template>

<script>
export default {
  name: "4_two_candidates",
  props: {
    data: []
  },
  data() {
    console.log('two_candidates',this.data)
      return {
        candidates: this.data
      }
  }
}
</script>

<style scoped>
.block {

    height: 100vh;

    background-image:url("../../assets/journalistScreens/4.png");

    display: flex;
    align-items: center;
    justify-content: center;
}
.photo{
  height: 56vh;
  width: 43vh;
}



</style>