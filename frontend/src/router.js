import { createWebHistory, createRouter } from "vue-router"
import Login from "./components/Login"
import CreateProtocol from "./components/CreateProtocol";
import Timer from "./components/Timer";
import ProtocolsList from "./components/ProtocolsList";
import UIKList from "./components/UIKList";
import TIKList from "./components/TIKList";
import ReadTIK from "./components/ReadTik";
import Turnout from "./components/Turnout";
import Demonstration from "./components/Demonstration";

const routes = [
  {
    path: "/demonstration",
    component: Demonstration,
  },
  {
    name: "createProtocol",
    path: "/protocol/create",
    component: CreateProtocol,
  },
  {
    name: "/protocols",
    path: "/protocols",
    component: ProtocolsList,
  },
  {
    name: "/uiks",
    path: "/uiks",
    component: UIKList,
  },
  {
    name: "/tiks",
    path: "/tiks",
    component: TIKList,
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
    name: "timer",
    path: "/timer",
    component: Timer,
  },
  {
    name: "/tik/read",
    path: "/tik/read",
    component: ReadTIK,
  },
  {
    name: "turnout",
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