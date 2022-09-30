import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../components/HomeView.vue'
import loginView from '../components/loginView.vue'
import search from '../components/search.vue'
import profileView from '../components/profileView.vue'
import groupsView from '../components/groupsView.vue'

const routes = [
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    component: loginView
  },
  {
    path: '/search',
    name: 'search',
    component: search
  },
  {
    path: '/profile',
    name: 'profile',
    component: profileView
  },
  {
    path: '/groups',
    name: 'groups',
    component: groupsView
  },
  {
    path: '/',
    redirect: '/home'
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
