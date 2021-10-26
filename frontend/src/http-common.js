import axios from "axios";

export default axios.create({
  baseURL: process.env.VUE_APP_DOMAIN + "/api/",
  headers: {
    "Content-type": "application/json"
  }
});