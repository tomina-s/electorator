import axios from '../http-common'
import authHeader from "./auth-header";

class UIKService {
  GetUIKList(page) {
    return axios
      .get(`/uiks/available/list/${page}/`, {
        headers: authHeader()
      })
      .then(response => {
          console.log(response.data)

          return response.data
      })
  }
  GetUIKQuantity() {
    return axios
      .get("/uiks/available/quantity/", {
        headers: authHeader()
      })
      .then(response => {
          console.log(response.data)

          return response.data
      })
  }
}

export default new UIKService()