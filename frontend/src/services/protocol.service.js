import axios from '../http-common'
import authHeader from "./auth-header";

class ProtocolService {
  SendProtocolFirst(protocol) {
    return axios
      .post("/protocols/first/", protocol, {
        headers: authHeader()
      })
      .then(response => {
          console.log(response.data)

          return response.data
      })
  }
  SendProtocolSecond(protocol) {
      return axios
          .post("/protocols/second/", protocol, {
              headers: authHeader()
          })
          .then(response => {
              console.log(response.data)

              return response.data
          })
  }
  GetProtocolFirstList(uik, page) {
      return axios
      .get(`/uiks/${uik}/protocols/first/list/${page}/`, {
          headers: authHeader()
      })
      .then(response => {
          console.log(response.data)

          return response.data
      })
  }
  GetProtocolFirstQuantity(uik) {
      return axios
      .get(`/uiks/${uik}/protocols/first/quantity/`, {
          headers: authHeader()
      })
      .then(response => {
          console.log(response.data)

          return response.data
      })
  }
}

export default new ProtocolService()