import axios from '../http-common'
import authHeader from "./auth-header";

class AuthService {
  login(account) {
    return axios
      .post('accounts/', {
        username: account.username,
        password: account.password
      })
      .then(response => {
        console.log(response.data)
        if (response.data.jwt) {
          localStorage.setItem('account', JSON.stringify(response.data))
        }

        return response.data
      })
  }
  getPermissions() {
    return axios
      .get('permissions/', {
        headers: authHeader(),
      })
      .then(response => {
        console.log(response.data)
        if (response.data.permissions) {
          localStorage.setItem('permissions', JSON.stringify(response.data.permissions))
        }

        return response.data
      })
  }
  getRole() {
    return axios
      .get('roles/', {
        headers: authHeader(),
      })
      .then(response => {
        console.log(response.data)
        if (response.data.role) {
          localStorage.setItem('role', JSON.stringify(response.data.role))
        }

        return response.data
      })
  }

  logout() {
    localStorage.removeItem('account')
    localStorage.removeItem('role')
    localStorage.removeItem('permissions')
  }
}

export default new AuthService()