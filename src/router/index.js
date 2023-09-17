import { createRouter, createWebHistory } from "vue-router"
const routes = [
{
path: "/",
name: "Home",
component: () => import("../views/home.vue"),
},
{
path: "/blog",
name: "Blog",
component: () => import("../views/blog.vue"),
},
{
path: "/works",
name: "Works",
component: () => import("../views/works.vue"),
},
{
path: "/contact",
name: "Contact",
component: () => import("../views/contact.vue"),
},
]
const router = createRouter({
history: createWebHistory(),
routes,
})
export default router
