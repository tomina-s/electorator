import axios from '../http-common'
import authHeader from "./auth-header"

class DemonstrationService {
  GeneralInfo() {
    return axios
      .get('generalinfo/', {
        headers: authHeader()
      })
      .then(response => {
        console.log(response.data)

        return response.data
      })
  }
}

export default new DemonstrationService()