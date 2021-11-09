<template>
  <div id="app">
    <nav
        class="navbar navbar-expand navbar-dark bg-dark"
        v-if="$route.path!=='/demonstration'"
    >
      <a href="/" class="navbar-brand">Main</a>
      <div class="navbar-nav mr-auto">
        <li class="nav-item">
          <router-link v-if="currentUser" to="/protocol/create" class="nav-link">Протокол</router-link>
        </li>
        <li class="nav-item">
          <router-link v-if="currentUser" to="/protocol/voters" class="nav-link">Внести явку</router-link>
        </li>
        <li class="nav-item">
          <router-link v-if="ableToOpen" to="/timer" class="nav-link">Открыть участок</router-link>
        </li>
        <li class="nav-item">
          <router-link  to="/demonstration" class="nav-link">Демонстрация</router-link>
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
          'height': '100vh'
        }"
    >
      <router-view :key="$route.fullPath"/>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    ableToOpen() {
      const currentTime = new Date().getTime()
      const openUpTo = 11
      const timeLeft = currentTime - currentTime % (1000 * 60 * 60 * 24) + openUpTo * 1000 * 60 * 60
      return timeLeft > 0
    },
    currentUser() {
      return this.$store.state.auth.account
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