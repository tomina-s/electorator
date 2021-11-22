<template>
  <div class = "block align-items-start ">
    <div class = "container-fluid text-white mt-2 pl-4 pr-5">
      <div class = "row ">
        <div class = "col-3 " v-for="(el, i) in candidates.slice(0,1)" :key="i">
          <img class="photo" :src="el.photo"/>
        </div>
        <div class = "col-3 pl-4" v-for="(el, i) in candidates.slice(0,1)" :key="i">
          <p class = "h3 font-weight-light">{{el.birthday}} г.р.</p>
          <div class = "h4">
            Место рождения:
            <br>
            {{el.birthday_place}}</div>

          <div class = "h4">
            Образование:
            <br>
             {{el.education}}
          </div>
         <div class = "h4">
            Основное место работы:
            <br>
            {{el.work}}</div>
          <div class = "h4">
             Занимаемая должность:
            <br>
            {{el.position}}</div>
        </div>
        <div class = "col-3 text-right " v-for="(el, i) in candidates.slice(1,2)" :key="i">
          <div class = "h3 font-weight-light">{{el.birthday}} г.р.
          </div>
         <div class = "h4">
            Место рождения:
            <br>
            {{el.birthday_place}}</div>
          <div class = "h4">
            Образование:
            <br>
             {{el.education}}
          </div>
          <div class = "h4">
            Основное место работы:
            <br>
            {{el.work}}</div>
          <div class = "h4">
             Занимаемая должность:
            <br>
            {{el.position}}</div>
        </div>
        <div class = "col-3" v-for="(el, i) in candidates.slice(1,2)" :key="i">
           <img class="photo ml=0" :src="el.photo"/>
        </div>
      </div>
      <br>
      <div class="row mt-3">
          <div class="col-6 " v-for="(el, i) in candidates.slice(0,1)" :key="i">
            <div class="h1">{{el.name}}</div>
            <br>
            <div class ="h3 font-weight-bold">{{el.party}}</div>
            <div class ="h3">{{el.polit_position}}</div>
          </div>
          <div class="col-6 text-right " v-for="(el, i) in candidates.slice(1,2)" :key="i">

            <div class="h1">{{el.name}}</div>
            <br>
            <div class="h3 font-weight-bold">{{el.party}}</div>
            <div class = "h3">{{el.polit_position}}</div>

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
    background-size: 100% auto;

    display: flex;
    align-items: center;
    justify-content: center;
}
.photo{
  height: 54.5vh;
  width: 43vh;

}



</style>