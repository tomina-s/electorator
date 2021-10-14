import { createWebHistory, createRouter } from "vue-router"
import Home from "./components/Home.vue"
import Login from "./components/Login.vue"

const routes = [
  {
    path: "/",
    component: Home,
  },
  {
    path: "/home",
    component: Home,
  },
  {
    path: "/login",
    component: Login,
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