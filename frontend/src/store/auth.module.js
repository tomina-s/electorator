import AuthService from '../services/auth.service'

const account = JSON.parse(localStorage.getItem('account'))
const initialState = account
  ? { status: { loggedIn: true }, account }
  : { status: { loggedIn: false }, account: null }

export const auth = {
  namespaced: true,
  state: initialState,
  actions: {
    login({ commit }, account) {
      return AuthService.login(account).then(
        account => {
          commit('loginSuccess', account)
          return Promise.resolve(account)
        },
        error => {
          commit('loginFailure')
          return Promise.reject(error)
        }
      )
    },
    logout({ commit }) {
      AuthService.logout()
      commit('logout')
    },
  },
  mutations: {
    loginSuccess(state, account) {
      state.status.loggedIn = true
      state.account = account
    },
    loginFailure(state) {
      state.status.loggedIn = false
      state.account = null
    },
    logout(state) {
      state.status.loggedIn = false
      state.account = null
    },
  }
}