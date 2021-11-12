import axios from '../http-common'
import authHeader from "./auth-header";

class TIKService {
  GetTIKList(page) {
    return axios
      .get(`/tiks/available/list/${page}/`, {
        headers: authHeader()
      })
      .then(response => {
          console.log(response.data)

          return response.data
      })
  }
  GetTIKQuantity() {
    return axios
      .get("/tiks/available/quantity/", {
        headers: authHeader()
      })
      .then(response => {
          console.log(response.data)

          return response.data
      })
  }
  GetTIK(name) {
    return axios
      .get(`/tiks/name/${encodeURIComponent(name)}/`, {
        headers: authHeader()
      })
      .then(response => {
          console.log(response.data)

          return response.data
      })
  }
  GetTIKCandidates(name) {
    return axios
      .get(`/tiks/name/${encodeURIComponent(name)}/candidates/`, {
        headers: authHeader()
      })
      .then(response => {
          console.log(response.data)

          return response.data
      })
  }
}

export default new TIKService()