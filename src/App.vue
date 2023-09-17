<script setup>
  import Navbar from '/src/components/navbar.vue'
  import Footer from '/src/components/footer.vue'
</script>
<template>
  <div>
    <Navbar/>
    <div class="content">
      <router-view v-slot="{ Component }">
        <transition name="fade">
          <keep-alive>
            <component :is="Component" />
          </keep-alive>
        </transition>
      </router-view>
    </div>
    <Footer/>
  </div>
</template>
<style scoped>
/* .fade-leave-to, */
.fade-enter-from {
  /*定义进入开始和离开结束的透明度为0*/
  opacity: 0;
}

/* .fade-leave-to {
  transform: translateX(20px);
} */

.fade-enter-to {
  transform: translateX(-20px);
}
/* .fade-leave-from, */
.fade-enter-to {
  /*定义进入结束和离开开始的透明度为1*/
  opacity: 1;
}

/* .fade-leave-active, */
.fade-enter-active {
  transition: all 0.5s ease-out;
}
</style>