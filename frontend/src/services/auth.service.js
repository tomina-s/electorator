import axios from '../http-common'

class AuthService {
  login(account) {
    return axios
      .post('/account/login', {
        snils: account.snils,
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

  logout() {
    localStorage.removeItem('account')
  }
}

export default new AuthService()