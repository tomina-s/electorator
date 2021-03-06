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
   GeneralInfoPresence(){
    return axios
        .get('generalinfopresence/',{
      headers:authHeader()
      })
        .then(response => {
          console.log(response.data)

          return response.data
        })
  }
  Presence(){
    return axios
        .get('presence/',{
      headers:authHeader()
      })
        .then(response => {
          console.log(response.data)

          return response.data
        })
  }
  TopPresence(){
    return axios
        .get('toppresence/',{
      headers:authHeader()
      })
        .then(response => {
          console.log(response.data)

          return response.data
        })
  }
    VotesPresence(){
    return axios
        .get('votespresence/',{
      headers:authHeader()
      })
        .then(response => {
          console.log(response.data)

          return response.data
        })
  }
    Top24Presence(){
    return axios
        .get('top24presence/',{
      headers:authHeader()
      })
        .then(response => {
          console.log(response.data)

          return response.data
        })
  }




}

export default new DemonstrationService()