<template>
  <div class="col-md-12">
    <div class="card card-container">
      <Form @submit="handleProtocol" :validation-schema="schema">
        <div class="form-group">
          <label class="font-weight-bold" for="num_uik">Номер УИК</label>
          <Field name="num_uik" type="text" class="form-control" />
          <ErrorMessage name="num_uik" class="error-feedback" />
        </div>
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
          <button class="btn btn-primary btn-block" :disabled="loading">
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
      </Form>
    </div>
  </div>
</template>

<script>
import { Form, Field, ErrorMessage } from "vee-validate"
import * as yup from "yup"
import ProtocolService from "../services/protocol.service"

export default {
  name: "Protocol",
  components: {
    Form,
    Field,
    ErrorMessage,
  },
  data() {
    console.log("data")
    const candidates = [{id: 3, name: "Кандидат Петров"}, {id: 32, name: "Кандидат Владимиров"}]
    let requiredFields = {
      num_uik: yup.string().required("Введите номер УИК"),
      sum_bul: yup.number().required("Поле обязательно").min(0, "Значение не может быть меньше 0"),
      bad_form: yup.number().required("Поле обязательно").min(0, "Значение не может быть меньше 0"),
    }
    candidates.forEach(candidate => {
      requiredFields[`can:${candidate.id}`] = yup.number().required("Поле обязательно").min(0, "Значение не может быть меньше 0")
    })

    const schema = yup.object().shape(
          requiredFields
      )
    console.log(schema)

    return {
      candidates: candidates,
      loading: false,
      message: "",
      schema,
    }
  },
  computed: {
  },
  created() {
  },
  methods: {
    handleProtocol(protocol) {
      protocol.status = protocol.status === true
      console.log(protocol)
      console.log("handling protocol")
      this.loading = true

      ProtocolService.SendProtocolOne(protocol)
          .then(() => {this.loading = false})
          .catch(e => {
            this.loading = false
            console.log(e)
          })
    },
  },
}

</script>