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
}

export default new ProtocolService()