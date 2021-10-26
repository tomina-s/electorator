<template>
  <div class="col-md-12">
    <div v-if="opened" class="card card-container ext-center display-3">
      Участок открыт
    </div>
    <div v-if="!opened" class="card card-container">
      <div class="text-center">
        <label v-if="!timeLeft" class="display-3">
          Откройте участок
        </label>
        <label v-if="timeLeft" class="display-3">
          {{ Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)) }}:
          {{ Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60)) }}:
          {{Math.floor((timeLeft % (1000 * 60)) / 1000)}}
        </label>
      </div>
      <Form @submit="handleOpening" :validation-schema="schema">
        <div class="form-group">
          <button class="btn btn-primary btn-block" :disabled="loading">
            <span
              v-show="loading"
              class="spinner-border spinner-border-sm"
            ></span>
            <span>Открыть участок</span>
          </button>
        </div>

        <div class="form-group">
          <div v-if="message" class="alert alert-danger" role="alert">
            {{ message }}
          </div>
        </div>

        <div class="form-group">
          <div v-if="info" class="alert alert-success" role="alert">
            {{ info }}
          </div>
        </div>
      </Form>
    </div>
  </div>
</template>

<script>
import ProtocolService from "../services/protocol.service"
import ConfigService from "../services/config.service";
import {getUIKPermission} from "../services/common.service";

export default {
  name: "Timer",
  data() {
    return {
      timeLeft: 0,
      loading: false,
      message: "",
      info: "",
      opened: false,
    }
  },
  computed: {
  },
  mounted() {
    // TODO проверять статус участка
  },
  created() {
    ConfigService.getTimeToOpen().then(
        data => {
          const openTime = data.timeToOpen * 1000
          const currentTime = new Date().getTime()
          this.timeLeft = openTime - currentTime
          this.countDownTimer()
        },
        error => {
          console.log(error)
        }
      )
  },
  methods: {
    handleOpening() {
      console.log(protocol)
      console.log("handling opening")
      this.loading = true

      const perm = getUIKPermission()
      if (!perm) {
        this.message = "Роль не соответствует выполняемым действиям"
        return
      }

      const protocol = {
        num_uik: perm,
        num_protocol_1: 0,
        status: true,
        sum_bul: 0,
        bad_form: 0,
      }

      ProtocolService.SendProtocolFirst(protocol)
          .then(() => {
            this.loading = false
            this.info = "Участок открыт"
          })
          .catch(e => {
            this.loading = false
            this.message = "Что-то пошло не так"
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