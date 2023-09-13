<script setup>
</script>
<template>
    <div id="app">
    <!--内容渲染-->
    <router-view></router-view>
    </div>
</template>

<style>
/*淡入动画效果*/
.slide-fade-enter-active {
    transition: opacity 1s, transform 1s;
  }
.slide-fade-enter
/* .slide-fade-leave-active 用于 2.1.8 以下版本 */ {
transform: translateX(10px);
opacity: 0;
}
</style>