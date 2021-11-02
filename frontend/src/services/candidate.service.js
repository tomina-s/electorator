import axios from '../http-common'
import authHeader from "./auth-header";

class CandidateService {
  GetCandidatesFromUIK() {
    return axios
      .get(`/uiks/candidates/short/list/`, {
        headers: authHeader()
      })
      .then(response => {
          console.log(response.data)

          return response.data
      })
  }
}

export default new CandidateService()