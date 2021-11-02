<template>
  <c1_opened
      v-if="state===1"
      :data="{opened: data.opened, voters: data.voters}"
  />
  <c2_candidates v-if="state===2"/>
</template>

<script>
import c1_opened from './journalistScreens/1_opened'
import c2_candidates from './journalistScreens/2_candidates'

export default {
  name: "Demonstration",
  components: {
    c1_opened,
    c2_candidates,
  },
  data() {
    return {
      state: 1,
      data: {
        opened: 12,
        voters: 13,
      }
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
          case 1:
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
        // this.state++
        this.countTimer()
      }, 3000)
    },
  }
}
</script>