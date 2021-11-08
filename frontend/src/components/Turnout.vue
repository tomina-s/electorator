<template>
  <div class="container" :style="{'background-color': 'transparent !important'}">
    <div class="col-md-12">
      <div class="card card-container" :style="{'background-color': 'transparent !important'}">
        <Form @submit="handleTurnout" :validation-schema="schema">
          <div class="form-group">
            <label class="font-weight-bold" for="num">Внести явку</label>
            <Field name="num" type="number" class="form-control" />
            <ErrorMessage name="num" class="error-feedback" />
          </div>

          <div class="form-group">
            <button class="btn btn-primary btn-block" :disabled="loading || globalError">
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
      </div>
    </div>
  </div>
</template>

<script>
import { Form, Field, ErrorMessage } from "vee-validate"
import * as yup from "yup"
import ProtocolService from "../services/protocol.service"
import {getUIKPermission} from "../services/common.service";

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
      globalError: false,
      innerNumber: 0,
      loading: false,
      message: "",
      info: "",
      schema,
    }
  },
  computed: {
  },
  mounted() {
    const perm = getUIKPermission()
    if (!perm) {
      this.globalError = true
      this.message = "Что-то пошло не так"
      return
    }
    ProtocolService.GetProtocolFirstQuantity(perm)
        .then(r => {
          this.innerNumber = r.quantity + 1
          if (r.quantity === 0) {
            this.$router.push("/timer")
          } else  if (r.quantity === 4){
            this.$router.push("/protocol/create")
          } else  if (r.quantity === 5){
            this.$router.push({ name: '/protocols', query: { uik_id: perm } })
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
        bad_form: 0,
      }

      ProtocolService.SendProtocolFirst(protocol)
          .then(() => {
            this.info = "Явка успешно зафиксирована"

            console.log(this.innerNumber)
            if (this.innerNumber === 4) {
              this.$router.push("/protocol/create")
              return
            }
            this.innerNumber++
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