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
<script setup>
import { onMounted, onBeforeUnmount } from 'vue';
  import Navbar from '/src/components/navbar.vue'
  import Footer from '/src/components/footer.vue'

  onMounted(() => {
  changeTitleOnVisibility();
});

onBeforeUnmount(() => {
  document.removeEventListener('visibilitychange', handleVisibilityChange);
});

function changeTitleOnVisibility() {
  const handleVisibilityChange = () => {
    if (document.visibilityState === 'visible') {
      document.title = 'Walkiiiy -within cells interlinked';
    } else {
      document.title = '+_+';
    }
  };

  document.addEventListener('visibilitychange', handleVisibilityChange);
};
</script>
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