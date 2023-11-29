import { createApp } from 'vue'
import router from './router'
import App from './App.vue'
import VueLazyLoad from 'vue3-lazyload'

const app = createApp(App)
app.use(router)
app.use(VueLazyLoad, {
    // options...
  })
app.mount('#app')
