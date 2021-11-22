<template>
  <div>
    <transition name="component-fade" mode="out-in">
      <component
          :key="counter"
          v-bind:is="slide"
          v-bind="currentData"
      >
      </component>
    </transition>
  </div>

</template>

<script>
import c0_screen from './journalistScreens/0_screen'
import c1_opened from './journalistScreens/1_opened'
import c2_candidates from './journalistScreens/2_candidates'
import c4_two_candidates from './journalistScreens/4_two_candidates'
import c5_toptik from './journalistScreens/5_toptik'
import c6_general_info_presence from './journalistScreens/6_general_info_presence'
import c7_presence from './journalistScreens/7_presence'
import c8_toppresence from './journalistScreens/8_top_presence'
import c9_top24presence from './journalistScreens/9_top_24_presence'
import c11_votespresence from './journalistScreens/11_votespresence'
import c12_one_candidate from './journalistScreens/12_one_candidate'
import c17_votes from './journalistScreens/17_votes'
import DemonstrationService from './../services/demonstration.service'
import ConfigService from "../services/config.service";

export default {
  name: "Demonstration",
  data() {
    return {
      counter: 0,
      slide: c0_screen,
      state: 0,
      data: {},
      config: {}
    }
  },
  computed: {
    currentData() {
      return {'data': this.data}
    }
  },
  mounted() {
    ConfigService.getTimeToOpen().then(
        data => {
          this.config = data
        },
        error => {
          console.log(error)
        }
      )
  },
  created() {
    this.countTimer()
  },
  methods: {
    splitArray(array, by) {
      if (!(array instanceof Array)) {
        return []
      }
      let arrayOfArrays = [];
      while (array.length > 0) {
        let arrayElement = array.splice(0,by);
        arrayOfArrays.push(arrayElement);
      }
      return arrayOfArrays;
    },
    countTimer() {
      setTimeout(() => {
        if (this.state === 0 || this.state === 5 || this.state === 10) {
          const currentTime = new Date().getTime()
          if (currentTime > this.config.firstConference * 1000) {
            this.state = 10 //0
          } else if (currentTime > this.config.secondConference * 1000) {
            this.state = 5
          } else if (currentTime > this.config.thirdConference * 1000) {
            this.state = 10
          }
        }
        if (this.state === 1) return


        switch (this.state) {
          // 10 00
          case 0:
            DemonstrationService.GeneralInfo()
                .then(r => {
                  this.data = r
                  this.slide = c1_opened
                  this.state = 1
                })
                .catch(e =>{
                  console.log(e)
                })
            break
          case 1:
            DemonstrationService.ListCandidatesInfo()
                .then(r => {
                  this.data = this.splitArray(r, 5)
                  this.slide = c2_candidates
                  this.state = 2
                })
                .catch(e =>{
                  console.log(e)
                })
            break
          case 2:
            this.data.splice(0, 2)
            if (this.data.length === 0) {
              this.slide = c0_screen
              this.state = 3
            }
            break
          case 3:
            DemonstrationService.ListCandidatesInfo()
                .then(r => {
                  this.data = r
                  this.slide = c4_two_candidates
                  this.state = 4
                })
                .catch(e =>{
                  console.log(e)
                })

            break
          case 4:
            this.data.splice(0, 2)
            if (this.data.length === 0) {
              DemonstrationService.TopTik()
                .then(r => {
                  this.data = r
                  this.slide = c5_toptik
                  this.state = 5
                })
                .catch(e =>{
                  console.log(e)
                })
            }
            break
            // 12 00, 15 00, 18 00
          case 5:
            this.slide = c0_screen
            this.state = 6
            break
          case 6:
            DemonstrationService.GeneralInfoPresence()
                .then(r => {
                  this.data = r
                  this.slide = c6_general_info_presence
                  this.state = 7
                })
                .catch(e =>{
                  console.log(e)
                })
            break
          case 7:
            DemonstrationService.Presence()
                .then(r => {
                  this.data = this.splitArray(r, 8)
                  this.slide = c7_presence
                  this.state = 8
                })
                .catch(e =>{
                  console.log(e)
                })
            break
          case 8:
            this.data.splice(0, 2)
            if (this.data.length === 0) {
              DemonstrationService.TopPresence()
                  .then(r => {
                    this.data = r
                    this.slide = c8_toppresence
                    this.state = 9
                  })
                  .catch(e =>{
                    console.log(e)
                  })
            }
            break
          case 9:
            DemonstrationService.Top24Presence()
                .then(r => {
                  this.data = r
                  this.slide = c9_top24presence
                  this.state = 10
                })
                .catch(e =>{
                  console.log(e)
                })
            break
            // 21 00
          case 10:
            this.slide = c0_screen
            this.state = 11
            break
          case 11:
            DemonstrationService.VotesPresence()
                .then(r => {
                  this.data = r
                  this.slide = c11_votespresence
                  this.state = 12
                })
                .catch(e =>{
                  console.log(e)
                })
            break
          case 12:
            DemonstrationService.ListCandidatesInfo()
                .then(r => {
                  this.data = r
                  this.slide = c12_one_candidate
                  this.state = 13 //13
                })
                .catch(e =>{
                  console.log(e)
                })
            break
          case 13:
            DemonstrationService.TopTik()
                .then(r => {
                  this.data = r
                  this.slide = c5_toptik
                  this.state = 16
                })
                .catch(e =>{
                  console.log(e)
                })
            break
          case 14:
            break
          case 15:
            break
          case 16:
            DemonstrationService.TopPresence()
                .then(r => {
                  this.data = r
                  this.slide = c8_toppresence
                  this.state = 17
                })
                .catch(e =>{
                  console.log(e)
                })

            break
          case 17:
            DemonstrationService.ListCandidatesInfo()
                .then(r => {
                  this.data = this.splitArray(r, 5)
                  this.slide = c17_votes
                  this.state = 18
                })
                .catch(e =>{
                  console.log(e)
                })
            break
          case 18:
            this.data.splice(0, 2)
            if (this.data.length === 0) {
              this.slide = c0_screen
              this.state = 0
            }
            break
       }
        this.counter++
        this.countTimer()
      }, 3000)
    },
  }
}
</script>