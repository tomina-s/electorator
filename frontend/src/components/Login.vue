<template>
  <div class="col-md-12">
    <div class="card card-container">
      <div class="display-4 text-center">
        Вход в систему
      </div>
      <Form @submit="handleLogin" :validation-schema="schema">
        <div class="form-group">
          <label for="username">Имя пользователя</label>
          <Field v-on:input="clearErrors" name="username" type="text" class="form-control" />
          <ErrorMessage name="username" class="error-feedback" />
        </div>
        <div class="form-group">
          <label for="password">Пароль</label>
          <Field v-on:input="clearErrors" name="password" type="password" class="form-control" />
          <ErrorMessage name="password" class="error-feedback" />
        </div>

        <div class="form-group">
          <button class="btn btn-primary btn-block" :disabled="loading">
            <span
              v-show="loading"
              class="spinner-border spinner-border-sm"
            ></span>
            <span>Войти</span>
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

export default {
  name: "Login",
  components: {
    Form,
    Field,
    ErrorMessage,
  },
  data() {
    const schema = yup.object().shape({
      username: yup.string().required("СНИЛС обязателен для ввода"),
      password: yup.string().required("Пароль обязателен для ввода"),
    })

    return {
      loading: false,
      message: "",
      schema,
    }
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn
    },
  },
  created() {
    if (this.loggedIn) {
      this.$router.push("/home")
    }
  },
  methods: {
    clearErrors() {
      this.message = ""
    },
    handleLogin(user) {
      this.message = ""
      console.log("handling login")
      this.loading = true

      this.$store.dispatch("auth/login", user).then(
        (r) => {
          console.log(r)
          if (r.role === "УИК" && r.permissions.length !== 0) {
            this.$router.push({ name: '/protocols', params: { uik_id: r.permissions[0] } })
          } else if (r.role === "ТИК" && r.permissions.length !== 0) {
            this.$router.push({ name: '/uiks' })
          } else if (r.role === "ЦИК") {
            this.$router.push({ name: '/uiks' })
          } else {
            this.$store.dispatch('auth/logout')
            this.message = "Похоже, уровень доступа для данного аккаунта " +
                "настроен неверно. Обратитесь к администратору"
          }
        },
        (error) => {
          this.loading = false
          console.log(error)
          this.message = "Войти не удалось, попробуйте снова"
        }
      )
    },
  },
}
</script>