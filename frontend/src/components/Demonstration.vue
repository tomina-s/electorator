<template>
  <div class="bg-image"
       :style="{
          'background-image': `url(${require('../assets/gradient.png')})`,
          'height': '100vh'
        }"
  >
    <transition name="component-fade" mode="out-in">
      <component v-bind:is="slide" v-bind="currentData"></component>
    </transition>
  </div>

</template>

<script>
import c0_screen from './journalistScreens/0_screen'
import c1_opened from './journalistScreens/1_opened'
import c2_candidates from './journalistScreens/2_candidates'
import DemonstrationService from './../services/demonstration.service'

export default {
  name: "Demonstration",
  components: {
    c0_screen,
    c1_opened,
    c2_candidates,
  },
  data() {
    return {
      slide: c0_screen,
      state: 0,
      data: {}
    }
  },
  computed: {
    currentData() {
      return {'data': this.data}
    }
  },
  mounted() {
  },
  created() {
    this.countTimer()
  },
  methods: {
    countTimer() {
      setTimeout(() => {
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
            this.slide = c0_screen
            this.state = 0
            break
          case 2:
            this.state = 0
            break
          case 3:
            break
          case 4:
            break
            // 12 00, 15 00, 18 00
          case 5:
            break
          case 6:
            break
          case 7:
            break
          case 8:
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
        this.countTimer()
      }, 3000)
    },
  }
}
</script>