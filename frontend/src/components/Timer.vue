<template>
  <div class="container" :style="{'background-color': 'transparent !important'}">
    <div class="col-md-12 text-white">
      <div class="card card-container" :style="{'background-color': 'transparent !important'}">
        <div v-if="!opened" class="text-center">
          <label v-if="!timeLeft || timeLeft < 0" class="display-3">
            Откройте участок
          </label>
          <label v-if="timeLeft > 0" class="display-3">
            {{ Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)) }}:
            {{ Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60)) }}:
            {{Math.floor((timeLeft % (1000 * 60)) / 1000)}}
          </label>
        </div>
        <div v-if="opened" class="card card-container text-center display-3"
             :style="{'background-color': 'transparent !important'}">
          Участок открыт
        </div>
        <Form @submit="handleOpening" :validation-schema="schema">
          <div class="form-group">
            <button class="btn btn-light btn-block" :disabled="loading || globalError">
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

        <switcher :key="innerNumber" :uik_id="perm" :protocolNum="1" :done="innerNumber > 1"/>
      </div>
    </div>
  </div>
</template>

<script>
import Switcher from "./Switcher"
import ProtocolService from "../services/protocol.service"
import ConfigService from "../services/config.service";
import {getRole, getUIKPermission} from "../services/common.service";

export default {
  name: "Timer",
  components: {
    Switcher
  },
  data() {
    return {
      globalError: false,
      perm: undefined,
      innerNumber: 0,
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
    const role = getRole()
    if (role !== "УИК") {
      this.globalError = true
    }
    let perm = this.$route.query.uik_id
    if (!perm) {
      perm = getUIKPermission()
    }

    if (!perm) {
      this.globalError = true
      this.message = "Что-то пошло не так"
      return
    }
    this.perm = perm

    ProtocolService.GetProtocolFirstQuantity(perm)
        .then(r => {
          this.innerNumber = r.quantity + 1
          if (r.quantity !== 0) {
            // this.$router.push({ name: '/protocols', query: { uik_id: perm } })
            this.globalError = true
            this.opened = true
          }
        })
        .catch(e => {
          console.log(e)
          this.globalError = true
          this.message = "Что-то пошло не так"
        })
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
            this.info = "Протокол отправлен"
            this.$router.push("/protocol/voters")
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