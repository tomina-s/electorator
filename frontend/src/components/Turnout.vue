<template>
  <div class="container" :style="{'background-color': 'transparent !important'}">
    <div class="col-md-12">
      <div class="card card-container text-white" :style="{'background-color': 'transparent !important'}">
        <span class="text-center display-3">Отчет о явке №{{innerNumber - 1}}</span>
        <Form @submit="handleTurnout" :validation-schema="schema">
          <div class="form-group">
            <label class="font-weight-bold" for="num">Внести явку<span style="color: orange">*</span></label>
            <Field name="num" type="number" class="form-control"
              :aria-readonly="globalError" :value="oldValue !== undefined ? oldValue : ''" :key="oldValue"
            />
            <ErrorMessage name="num" class="error-feedback" />
          </div>

          <div class="form-group">
            <button class="btn btn-light btn-block" :disabled="loading || globalError">
              <span
                v-show="loading"
                class="spinner-border spinner-border-sm"
              ></span>
              <span>Отправить протокол</span>
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
        <switcher :key="innerNumber" :uik_id="perm" :protocolNum="innerNumber" :done="oldValue !== undefined"/>
      </div>
    </div>
  </div>
</template>

<script>
import Switcher from "./Switcher"
import { Form, Field, ErrorMessage } from "vee-validate"
import * as yup from "yup"
import ProtocolService from "../services/protocol.service"
import {getRole, getUIKPermission} from "../services/common.service";

export default {
  name: "Turnout",
  components: {
    Form,
    Field,
    ErrorMessage,
    Switcher,
  },
  data() {
    const schema = yup.object().shape({
      num: yup.number().integer("Ожидается целое число").typeError('Ожидается число').required("Укажите явку")
          .min(0, "Значение не может быть меньше 0").max(30000000, "Значение не может быть меньше 30000000"),
    })

    return {
      perm: undefined,
      oldValue: undefined,
      globalError: false,
      innerNumber: this.$route.query.protocolNum ? parseInt(this.$route.query.protocolNum) : 0,
      nextProtocolNumber: 0,
      loading: false,
      message: "",
      info: "",
      schema,
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

    ProtocolService.GetProtocolFirstList(perm, 1)
        .then(r => {
          const quantity = r.length
          if (!this.innerNumber) {
            this.innerNumber = quantity >= 4 ? 4 : quantity + 1
          }
          this.nextProtocolNumber = quantity + 1

          if (this.innerNumber < this.nextProtocolNumber) {
            this.info = "Протокол был успешно отправлен"
            this.oldValue = r[this.innerNumber - 1].sum_bul
            this.globalError = true
          } else if (this.innerNumber > this.nextProtocolNumber) {
            this.globalError = true
            this.message = "Предыдущий протокол еще не был отправлен"
          }
        })
        .catch(e => {
          this.globalError = true
          console.log(e)
          this.message = "Что-то пошло не так"
        })
  },
  methods: {
    handleTurnout(num) {
      console.log(num)
      console.log("handling turnout")
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
        sum_bul: num.num,
        sum_final_bul: 0,
        bad_form: 0,
      }

      ProtocolService.SendProtocolFirst(protocol)
          .then(() => {
            this.info = "Явка успешно зафиксирована"

            console.log(this.innerNumber)
            this.innerNumber++
            if (this.innerNumber === 5) {
              this.$router.push("/protocol/create")
              return
            } else {
              this.$router.push({ name:'turnout', query:{ protocolNum:  this.innerNumber } })
            }
            this.loading = false
          })
          .catch(e => {
            this.loading = false
            this.message = "Не удалось зафиксировать явку"
            console.log(e)
          })
    },
  },
}

</script>