# 瀑布流vue组件vue-waterfall-easy
* 注意该组件基于vue2编写，不兼容vue3
* 实现代码：
```js
<template>
<div id="content">
    <vue-waterfall-easy :imgsArr="imgsArr"></vue-waterfall-easy>
</div>
</template>
  
  <script>
  import vueWaterfallEasy from 'vue-waterfall-easy'
    export default {
        name: 'app',
        data() {
          return {
            imgsArr: [
  { src: './photos/independence1.jpg',},
  { src: './photos/independence2.jpg',},
  { src: './photos/fred.jpeg',},
  { src: './photos/Jean.jpg',},
  { src: './photos/academy.jpg',},
            ],
          }
        },
        components: {
          vueWaterfallEasy
        },
        methods: {
        },
        created() {
        }
      }
  </script>
<style>
 #content{
  position: absolute;    /*必须*/
  top:32px;              /*top必须，大小可控制*/
  bottom:0;              /*bottom必须，一直延申到当前块底部*/
  width:100%;
}
</style>
```