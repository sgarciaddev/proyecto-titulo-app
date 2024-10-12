import { createRouter, createWebHistory } from 'vue-router';

import HomeView from '@/views/HomeView.vue';
import SimuladorView from '@/views/SimuladorView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/inicio'
    },
    {
      path: '/inicio',
      name: 'inicio',
      component: HomeView
    },
    {
      path: '/simulador',
      name: 'simulador',
      component: SimuladorView
    }
  ],
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) {
      return {
        el: to.hash,
        behavior: 'smooth'
      };
    }
    return savedPosition || { top: 0 };
  }
});

export default router;
