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
  TopTik(){
    return axios
        .get('toptik/',{
      headers:authHeader()
      })
        .then(responce => {
          console.log(responce.data)
        })
  }

}

export default new DemonstrationService()