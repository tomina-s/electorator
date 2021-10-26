import axios from '../http-common'
import authHeader from "./auth-header";

class CandidateService {
  GetCandidatesFromUIK(uikID) {
    return axios
      .get(`/uik/${uikID}/candidates/short/list/`, {
        headers: authHeader()
      })
      .then(response => {
          console.log(response.data)

          return response.data
      })
  }
}

export default new CandidateService()