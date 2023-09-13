import { createWebHashHistory } from "vue-router";
import { createRouter } from "vue-router";
import home from '@/views/home.vue'

const router=createRouter({
    history:createWebHashHistory(),//路由模式
    routes:[
      {
        path: '/',
        redirect: '/home'
      },
      {
        path: '/home',
        name: 'home',
        component: home,
        meta: {
          index: 1
        }
      },
      {
        path: '/blog',
        name: 'blog',
        component: () => import('@/views/blog.vue'),
        meta: {
          index: 1
        }
      },
      {
        path: '/works',
        name: 'works',
        component: () => import('@/views/works.vue'),
        meta: {
          index: 1
        }
      },
      {
        path: '/contact',
        name: 'contact',
        component: () => import('@/views/contact.vue'),
        meta: {
          index: 1
        }
      },
    ]
})
export default router