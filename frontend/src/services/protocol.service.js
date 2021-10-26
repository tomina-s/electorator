import axios from '../http-common'
import authHeader from "./auth-header";

class ProtocolService {
  SendProtocolOne(protocol) {
    return axios
      .post("/protocols/first/", {
          num_uik: protocol.num_uik,
          status: protocol.status,
          sum_bul: protocol.sum_bul,
          bad_form: protocol.bad_form,
          num_protocol_1: protocol.num_protocol_1,
      }, {
        headers: authHeader()
      })
      .then(response => {
          console.log(response.data)

          return response.data
      })
  }
  SendProtocolTwo(protocol) {
    return axios
      .post("/protocol/two", {
          num_uik: protocol.num_uik,
          candidate_votes: protocol.candidate_votes,
      }, {
        headers: authHeader()
      })
      .then(response => {
          console.log(response.data)

          return response.data
      })
  }
  SendTurnout(num) {
    return axios
      .post("/protocol/voters", {
          num: num,
      }, {
        headers: authHeader()
      })
      .then(response => {
          console.log(response.data)

          return response.data
      })
  }
}

export default new ProtocolService()