<template>
  <div class="bg-image"
       :style="{
          'background-image': `url(${require('../assets/gradient.png')})`,
          'height': '100vh'
        }"
  >
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
import c5_toptik from './journalistScreens/5_toptik'
import c6_general_info_presence from './journalistScreens/6_general_info_presence'
import c7_presence from './journalistScreens/7_presence'
import c8_toppresence from './journalistScreens/8_top_presence'
import DemonstrationService from './../services/demonstration.service'
import ConfigService from "../services/config.service";

export default {
  name: "Demonstration",
  components: {
    c0_screen,
    c1_opened,
    c2_candidates,
    c5_toptik,
    c6_general_info_presence,

  },
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
    splitArray(array) {
      let arrayOfArrays = [];
        while (array.length > 0) {
            let arrayElement = array.splice(0,4);
            arrayOfArrays.push(arrayElement);
        }
        return arrayOfArrays;
    },
    countTimer() {
      setTimeout(() => {
        if (this.state === 0 || this.state === 5 || this.state === 10) {
          const currentTime = new Date().getTime()
          if (currentTime > this.config.firstConference * 1000) {
            this.state = 5 //0
          } else if (currentTime > this.config.secondConference * 1000) {
            this.state = 5
          } else if (currentTime > this.config.thirdConference * 1000) {
            this.state = 10
          }
        }

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
                  this.data = this.splitArray(r)
                  this.slide = c2_candidates
                  this.state = 2
                })
                .catch(e =>{
                  console.log(e)
                })
            break
          case 2:
            if (this.data.length !== 0) {
              console.log("before", this.data)
              this.data.splice(0, 2)
              console.log("after", this.data)
            } else {
              this.slide = c0_screen
              this.state = 4
            }
            break
          case 3:

            break
          case 4:
             DemonstrationService.TopTik()
                .then(r => {
                  this.data = r
                  this.slide = c5_toptik
                  this.state = 5
                })
                .catch(e =>{
                  console.log(e)
                })
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
            DemonstrationService.Presence() //не могу пока вывести массив
                .then(r => {
                  this.data = this.splitArray(r)
                  this.slide = c7_presence
                  this.state = 8
                })
                .catch(e =>{
                  console.log(e)
                })
            break
          case 8:
            DemonstrationService.TopPresence() //не могу пока вывести массив
                .then(r => {
                  this.data = r
                  this.slide = c8_toppresence
                  this.state = 0
                })
                .catch(e =>{
                  console.log(e)
                })
            break
          case 9:
            break
            // 21 00
          case 10:

            break
          case 11:
            break
          case 12:
            break
          case 13:
            break
          case 14:
            break
          case 15:
            break
          case 16:
            break
          case 17:
            break
          case 18:
             break
       }
        this.counter++
        this.countTimer()
      }, 3000)
    },
  }
}
</script>