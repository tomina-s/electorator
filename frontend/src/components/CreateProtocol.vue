<template>
  <div class="container" :style="{'background-color': 'transparent !important'}">
    <div class="col-md-12">
      <div class="card card-container text-white" :style="{'background-color': 'transparent !important'}">
        <span class="text-center display-3">Итоговый протокол</span>
        <Form @submit="handleProtocol" :validation-schema="schema">
          <div class="form-group">
            <label class="font-weight-bold" for="sum_bul_fin">Число обработанных бюллетеней</label>
            <Field name="sum_bul" type="number" class="form-control"
              :aria-readonly="globalError" :value="oldValue !== undefined ? oldValue.sum_bul : ''" :key="oldValue"/>
            <ErrorMessage name="sum_bul" class="error-feedback" />
          </div>
          <div class="form-group">
            <label class="font-weight-bold" for="bad_form">Число испорченных бюллетеней</label>
            <Field name="bad_form" type="number" class="form-control"
              :aria-readonly="globalError" :value="oldValue !== undefined ? oldValue.bad_form : ''" :key="oldValue"/>
            <ErrorMessage name="bad_form" class="error-feedback" />
          </div>

          <div
            v-for="(candidate, i) in candidates"
            :key="candidate.id"
            class="form-group"
          >
            <label class="font-weight-bold" :for="`can:${candidate.id}`">{{candidate.name}}</label>
            <Field :name="`can:${candidate.id}`" type="number" class="form-control" :key="oldValue"
              :aria-readonly="globalError" :value="oldValue !== undefined ? oldValue.candidates[i].candidate_votes : ''"/>
            <ErrorMessage :name="`can:${candidate.id}`" class="error-feedback" />
          </div>


          <div class="form-group">
            <button class="btn btn-light btn-block" :disabled=isDisabled>
              <span
                v-show=isLoading
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
import CandidateService from "../services/candidate.service"
import {getRole, getUIKPermission} from "../services/common.service"

export default {
  name: "Protocol",
  components: {
    Form,
    Field,
    ErrorMessage,
    Switcher,
  },
  data() {
    return {
      perm: undefined,
      oldValue: undefined,
      innerNumber: 5,
      nextProtocolNumber: 0,
      globalError: false,
      candidates: [],
      loading: false,
      message: "",
      info: "",
      schema: {},
    }
  },
  computed: {
    isLoading() {
      return this.loading || this.candidates.length === 0
    },
    isDisabled() {
      return this.loading || this.candidates.length === 0
          || this.globalError
    }
  },
  created() {
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

    CandidateService.GetCandidatesFromUIK()
        .then(r => {
          this.candidates = r

          let requiredFields = {
            sum_bul_fin: yup.number().typeError('Ожидается число').required("Поле обязательно").min(0, "Значение не может быть меньше 0"),
            bad_form: yup.number().typeError('Ожидается число').required("Поле обязательно").min(0, "Значение не может быть меньше 0"),
          }
          this.candidates.forEach(candidate => {
            requiredFields[`can:${candidate.id}`] = yup.number().typeError('Ожидается число').required("Поле обязательно").min(0, "Значение не может быть меньше 0")
          })

          this.schema = yup.object().shape(
            requiredFields
          )
        })
        .catch(e => {
          this.loading = false
          console.log(e)
        })

    ProtocolService.GetProtocolFirstList(perm, 1)
        .then(r => {
          const quantity = r.length
          this.nextProtocolNumber = quantity + 1

          if (this.innerNumber < this.nextProtocolNumber) {
            this.info = "Протокол был успешно отправлен"
            this.oldValue = r[this.innerNumber - 1]
            this.globalError = true
          } else if (this.innerNumber > this.nextProtocolNumber) {
            this.globalError = true
            this.message = "Заполните предыдущий протокол"
          }
        })
        .catch(e => {
          this.globalError = true
          console.log(e)
          this.message = "Что-то пошло не так"
        })
  },
  methods: {
    handleProtocol(protocol) {
      protocol.status = false
      protocol.num_protocol_1 = 0

      const perm = getUIKPermission()
      if (!perm) {
        this.message = "Роль не соответствует выполняемым действиям"
        return
      }

      protocol.num_uik = perm
      console.log(protocol)
      console.log("handling protocol")
      this.loading = true

      ProtocolService.SendProtocolFirst(protocol)
          .then(() => {this.loading = false})
          .catch(e => {
            this.message = "Отправить протокол не удалось"
            this.info = ""
            this.loading = false
            console.log(e)
          })

      this.candidates.forEach(v => {
        if (protocol[`can:${v.id}`] === "") {
          return
        }
        const votes = parseInt(protocol[`can:${v.id}`])

        const protocolSecond = {
          num_uik: perm,
          name: v.id,
          candidate_votes: votes,
        }
        ProtocolService.SendProtocolSecond(protocolSecond)
            .then(() => {
              this.loading = false
              this.info = "Явка успешно отправлена"
              this.message = ""

              this.$router.push({ name: '/protocols', query: { uik_id: perm } })
            })
            .catch(e => {
              this.message = "Отправить протокол не удалось"
              this.info = ""
              this.loading = false
              console.log(e)
            })
      })
    },
  },
}

</script>