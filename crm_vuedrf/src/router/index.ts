import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import store from '../store'

import SignUp from '../views/SignUp.vue'
import SignIn from '../views/SignIn.vue'
import Dashboard from '../views/dashboard/Dashboard.vue'
import MyAccount from '../views/dashboard/MyAccount.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/sign-in',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: { requiresAuth: true }
  },
  {
    path: '/dashboard/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta: { requiresAuth: true }
  },
  {
    path: '/about',
    name: 'about',
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.getters.isAuthenticated) {
      next({ name: 'SignIn' })
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router
