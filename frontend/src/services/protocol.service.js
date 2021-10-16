import axios from 'axios'

class ProtocolService {
  SendProtocolOne(protocol) {
    return axios
      .post("/protocol/one", {
          num_uik: protocol.num_uik,
          status: protocol.status,
          sum_bul: protocol.sum_bul,
          sum_final_bul: protocol.sum_final_bul,
          bad_form: protocol.bad_form,
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
      })
      .then(response => {
          console.log(response.data)

          return response.data
      })
  }
}

export default new ProtocolService()