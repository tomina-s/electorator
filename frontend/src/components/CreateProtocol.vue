<template>
  <div class="col-md-12">
    <div class="card card-container">
      <Form @submit="handleProtocol" :validation-schema="schema">
        <div class="form-group">
          <label class="font-weight-bold" for="status">Участок открыт</label>
          <Field name="status" type="checkbox" :value="true" true-value="true" false-value="false" class="form-control" />
          <ErrorMessage name="status" class="error-feedback" />
        </div>
        <div class="form-group">
          <label class="font-weight-bold" for="sum_bul">Проголосовало</label>
          <Field name="sum_bul" type="number" class="form-control" />
          <ErrorMessage name="sum_bul" class="error-feedback" />
        </div>
        <div class="form-group">
          <label class="font-weight-bold" for="bad_form">Бюллетеней испорчено</label>
          <Field name="bad_form" type="number" class="form-control" />
          <ErrorMessage name="bad_form" class="error-feedback" />
        </div>

        <div
          v-for="(candidate) in candidates"
          :key="candidate.id"
          class="form-group"
        >
          <label class="font-weight-bold" :for="`can:${candidate.id}`">{{candidate.name}}</label>
          <Field :name="`can:${candidate.id}`" type="number" class="form-control" />
          <ErrorMessage :name="`can:${candidate.id}`" class="error-feedback" />
        </div>


        <div class="form-group">
          <button class="btn btn-primary btn-block" :disabled=isLoading>
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
    </div>
  </div>
</template>

<script>
import { Form, Field, ErrorMessage } from "vee-validate"
import * as yup from "yup"
import ProtocolService from "../services/protocol.service"
import CandidateService from "../services/candidate.service"
import {getUIKPermission} from "../services/common.service"

export default {
  name: "Protocol",
  components: {
    Form,
    Field,
    ErrorMessage,
  },
  data() {
    return {
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
    }
  },
  created() {
  },
  mounted() {
    const perm = getUIKPermission()
    if (!perm) {
      this.message = "Роль не соответствует выполняемым действиям"
      return
    }
    CandidateService.GetCandidatesFromUIK(perm)
        .then(r => {
          this.candidates = r

          let requiredFields = {
            sum_bul: yup.number().required("Поле обязательно").min(0, "Значение не может быть меньше 0"),
            bad_form: yup.number().required("Поле обязательно").min(0, "Значение не может быть меньше 0"),
          }
          this.candidates.forEach(candidate => {
            requiredFields[`can:${candidate.id}`] = yup.number().required("Поле обязательно").min(0, "Значение не может быть меньше 0")
          })

          this.schema = yup.object().shape(
            requiredFields
          )
        })
        .catch(e => {
          this.loading = false
          console.log(e)
        })
  },
  methods: {
    handleProtocol(protocol) {
      protocol.status = protocol.status === true
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
        const votes = parseInt(protocol[`can:${v.id}`])
        if (!votes) {
          return
        }

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