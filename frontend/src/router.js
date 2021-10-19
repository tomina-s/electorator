import { createWebHistory, createRouter } from "vue-router"
import Login from "./components/Login"
import Protocol from "./components/Protocol";
import Timer from "./components/Timer";
import ProtocolsList from "./components/ProtocolsList";
import ReadProtocol from "./components/ReadProtocol";
import Turnout from "./components/Turnout";

const routes = [
  {
    path: "/protocol/create",
    component: Protocol,
  },
  {
    path: "/",
    component: ProtocolsList,
  },
  {
    path: "/home",
    component: ProtocolsList,
  },
  {
    path: "/login",
    component: Login,
  },
  {
    path: "/timer",
    component: Timer,
  },
  {
    path: "/protocol/read",
    component: ReadProtocol,
    props: {id: 0}
  },
  {
    path: "/protocol/voters",
    component: Turnout
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const publicPages = ['/login']
  const authRequired = !publicPages.includes(to.path)
  const loggedIn = localStorage.getItem('account')

  if (authRequired && !loggedIn) {
    console.log("go to next")
    next({
      path: '/login',
    })
  } else {
    next()
  }
})

export default router