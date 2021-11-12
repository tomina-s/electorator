<template>
  <div id="app">
    <nav
        class="navbar navbar-expand navbar-dark bg-dark"
        v-if="$route.path!=='/demonstration'"
    >
      <div class="navbar-nav mr-auto">
        <li class="nav-item">
          <router-link v-if="isUIK" to="/protocols" class="nav-link">Протоколы</router-link>
        </li>
        <li class="nav-item">
          <router-link v-if="isTIK || isCIK" to="/uiks" class="nav-link">Перейти к списку УИК</router-link>
        </li>
        <li class="nav-item">
          <router-link v-if="isCIK" to="/demonstration" class="nav-link">Демонстрация</router-link>
        </li>
        <li class="nav-item">
          <router-link v-if="isCIK" to="/tiks" class="nav-link">Перейти к списку ТИК</router-link>
        </li>
      </div>

      <div v-if="!currentUser" class="navbar-nav ml-auto">
        <li class="nav-item">
          <router-link to="/login" class="nav-link">
            <font-awesome-icon icon="sign-in-alt" /> Войти
          </router-link>
        </li>
      </div>

      <div v-if="currentUser" class="navbar-nav ml-auto">
        <li class="nav-item">
          {{ currentUser.name }}
        </li>
        <li class="nav-item">
          <a class="nav-link" @click.prevent="logOut">
            <font-awesome-icon icon="sign-out-alt" /> Выйти
          </a>
        </li>
      </div>
    </nav>

    <div class="bg-image"
       :style="{
          'background-image': `url(${require('./assets/gradient.png')})`,
          'background-repeat': 'no-repeat',
          'background-attachment': 'fixed',
          'background-position': 'center',
          'background-size': 'cover',
          'min-height': '100vh'
        }"
    >
      <router-view :key="$route.fullPath"/>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    currentUser() {
      return this.$store.state.auth.account
    },
    isUIK() {
      return this.$store.state.auth.account && this.$store.state.auth.account.role === "УИК"
    },
    isTIK() {
      return this.$store.state.auth.account && this.$store.state.auth.account.role === "ТИК"
    },
    isCIK() {
      return this.$store.state.auth.account && this.$store.state.auth.account.role === "ЦИК"
    },
  },
  methods: {
    logOut() {
      this.$store.dispatch('auth/logout')
      this.$router.push('/login')
    }
  }
};
</script>