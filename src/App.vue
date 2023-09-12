<script setup>
import {ref} from 'vue'
import blog from './components/blog.vue'
import home from './components/home.vue'
import works from './components/works.vue'
import contact from './components/contact.vue'
import { Transition } from 'vue'
const currentPage = ref(0)
const chose_page = (type)=> {
    currentPage.value = type
}
</script>

<template>
  <section id="app">
      <!-- 导航栏 -->
      <div class="flex_disply">
      <ol class="navbar">
          <li><button @click="chose_page(0)">home</button></li>
          <li><button @click="chose_page(1)">blog</button></li>
          <li><button @click="chose_page(2)">works</button></li>
      </ol>
      <ol class="contact">
          <li><button @click="chose_page(3)">contact</button></li>
      </ol>
      </div>
      <transition name="slide-fade">
      <div v-if="currentPage === 0">
        <home/>
      </div>
      </transition>
      <transition name="slide-fade">
      <div v-if="currentPage === 1">
        <blog/>
      </div>
      </transition>
      <transition name="slide-fade">
      <div v-if="currentPage === 2">
        <works/>
      </div>
      </transition>
      <transition name="slide-fade">
      <div v-if="currentPage === 3">
        <contact/>
      </div>
      </transition>

      <!--页脚-->
      <div id="bottom_line">
          <p>Welcome! This is the personal site of Walkiiiy.</p>
      </div>
    </section>
</template>

<style>
/* [v-cloak]{
    display:none;
} */
body {
    font-family: Arial, sans-serif; /* 使用 Arial 字体，如果不可用则使用 sans-serif 字体作为备选 */
    color: #333; /* 文字颜色为深灰色 */
}


/* 导航栏*/
.navbar {
    list-style-type: none; /* 去除默认的列表样式 */
    margin: 0;
    padding: 0;
    width: 80vw;
    height: 10vh;
    /*background-color: #a3a3a3; /* 导航栏背景颜色 */
}

.navbar li {
    display: inline-block; /* 将列表项显示为水平排列 */
}

.navbar li button {
    font-size:medium;
    border: none;
    background-color:rgb(255, 255, 255);
    padding: 5px 30px; /* 调整导航项的内边距 */
    color: #333; /* 导航项文字颜色 */
}

.contact{
    width: 20vw;
    position: absolute;
    top:0;
    right:0;
    list-style-type: none;
    height: 10vh;
}

.contact li button{
    position: absolute;
    top:0;
    right: 30px;
    font-size:medium;
    border: none;
    background-color:rgb(255, 255, 255);
    padding: 0px 0px;
    text-align: right;
    color: #333; /* 导航项文字颜色 */
}


/*页脚*/
#bottom_line{
    position: absolute;
    bottom: 10px;
    height: 5vh;
    width: 99vw;
}

#bottom_line p{
    text-align: center;
}

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