## vue_router

### vue2 router
* 安装：yarn add vue-router@^3.5.2
* src/router/index.js:
``` js
import VueRouter from 'vue-router';
const routes = [
{
path: "/",
name: "home",
component: () => import("../views/home.vue"),
},
]
const router = new VueRouter({
mode:'hash',
routes,
})
export default router;

```
* src/main.js:
``` js
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueRouter from 'vue-router'
Vue.config.productionTip = false
Vue.use(VueRouter);
new Vue({
  render: h => h(App),
  router,
}).$mount('#app')

```
* src/App.vue:
``` js
<template>
<div>
<navbar/>
<div>
      <router-view/>
</div>
<div style="height: 100%; width: 1vw;background-color:rgb(15, 15, 15); position: absolute; right:0"></div>
</div>
</template>
```



