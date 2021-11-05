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
        .then(response => {
          console.log(response.data)

          return response.data
        })
  }


  ListCandidatesInfo() {
    return axios
      .get('uiks/candidates/short/list/desc/', {
        headers: authHeader()
      })
      .then(response => {
        console.log(response.data)

        return response.data
      })
  }

}

export default new DemonstrationService()