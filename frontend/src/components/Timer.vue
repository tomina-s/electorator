<template>
  <div class="col-md-12">
    <div class="card card-container">
        <div class="text-center">
          <label class="display-3">
            {{ Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)) }}:
            {{ Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60)) }}:
            {{Math.floor((timeLeft % (1000 * 60)) / 1000)}}</label>
        </div>
      <Form @submit="handleOpening" :validation-schema="schema">
        <div class="form-group">
          <button class="btn btn-primary btn-block" :disabled="loading">
            <span
              v-show="loading"
              class="spinner-border spinner-border-sm"
            ></span>
            <span>Участок открыт</span>
          </button>
        </div>
      </Form>
    </div>
  </div>
</template>

<script>
import ProtocolService from "../services/protocol.service"
import ConfigService from "../services/config.service";

export default {
  name: "Timer",
  data() {
    return {
      timeLeft: 0,
      loading: false,
    }
  },
  computed: {
  },
  created() {
    // получать с сервера время открытия
    console.log('config')
    ConfigService.getTimeToOpen().then(
        data => {
          const openTime = data.timeToOpen * 1000
     // openTime = 0 //1634635800000
          const currentTime = new Date().getTime()
    console.log('this', this)
          this.timeLeft = openTime - currentTime
          this.countDownTimer()
        },
        error => {
          console.log(error)
        }
      )
  },
  methods: {
    handleOpening(protocol) {
      protocol.status = protocol.status === true
      console.log(protocol)
      console.log("handling opening")
      this.loading = true

      ProtocolService.SendProtocolOne(protocol)
          .then(() => {this.loading = false})
          .catch(e => {
            this.loading = false
            console.log(e)
          })
    },
    countDownTimer() {
      if(this.timeLeft > 0) {
        setTimeout(() => {
          this.timeLeft -= 1000
          this.countDownTimer()
        }, 1000)
      }
    },
  }
}
</script>