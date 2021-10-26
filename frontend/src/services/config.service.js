import axios from '../http-common'

class ConfigService {
  getTimeToOpen() {
    return axios
      .get("/config/")
      .then(response => {
          console.log(response.data)

          return response.data
      })
  }
}

export default new ConfigService()