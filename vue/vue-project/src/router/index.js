import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/home',
      name: 'Home',
      meta: {
        requiresAuth: true
      },
      component: HomeView
    },
    {
      path: '/me',
      name: 'Me',
      meta: {
        requiresAuth: true
      }
    }
  ]
});
// var isAuthenticated = false
// router.beforeEach(async(to, from)=>{
//   if(
//     !isAuthenticated &&
//     to.name !== 'login'
//   ) {
//     return { name: 'login' }
//   }
// })

export default router
