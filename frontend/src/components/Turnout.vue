<template>
  <div class="col-md-12">
    <div class="card card-container">
      <Form @submit="handleTurnout" :validation-schema="schema">
        <div class="form-group">
          <label class="font-weight-bold" for="num">Внести явку</label>
          <Field name="num" type="number" class="form-control" />
          <ErrorMessage name="num" class="error-feedback" />
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
  name: "Turnout",
  components: {
    Form,
    Field,
    ErrorMessage,
  },
  data() {
    const schema = yup.object().shape({
      num: yup.number().required("Укажите явку").min(0, "Значение не может быть меньше 0"),
    })

    return {
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
    handleTurnout(num) {
      console.log(num)
      console.log("handling turnout")
      this.loading = true

      ProtocolService.SendTurnout(num)
          .then(() => {this.loading = false})
          .catch(e => {
            this.loading = false
            console.log(e)
          })
    },
  },
}

</script>