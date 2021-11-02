import { createApp } from 'vue'
import App from './App.vue'
import router from "./router"
import store from "./store"
import "bootstrap"
import "bootstrap/dist/css/bootstrap.min.css"
import "css/fade.css"
import { FontAwesomeIcon } from './plugins/font-awesome'
import Pagination from 'v-pagination-3'

createApp(App)
    .use(router)
    .use(store)
    .component("font-awesome-icon", FontAwesomeIcon)
    .component('pagination', Pagination)
    .mount("#app");