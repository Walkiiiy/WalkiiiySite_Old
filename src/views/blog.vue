<template>
  <!--博客页-->
      <div>
      <h2>Walkiiiy's blog</h2>
      <ol id="blog_list">
          <li><a class="bloglink" href="blog/photos/photos_23_9_9.html">photos_23_9_9</a></li>
          <li><a class="bloglink" href="blog/js/js对象和方法.html">js对象和方法</a></li>
          <li><a class="bloglink" href="blog/vue/vue.js_工程化配置.html">vue.js与vite_工程化 配置</a></li>
          <li><a class="bloglink" href="blog/bds_manual.html">mc_bds_服务器手册</a></li>
          <li><a class="bloglink" href="blog/js/js箭头函数.html">js箭头函数</a></li>
          <li><a class="bloglink" href="blog/photos/photos_23_8_21.html">photos_23_8_21</a></li>
          <li><a class="bloglink" href="blog/js/vue_notebook.html">vue_notebook</a></li>
          <li><a class="bloglink" href="blog/js/js数组.html">js数组</a></li>
          <li><a class="bloglink" href="blog/c++/c++const.html">c++const</a></li>
          <li><a class="bloglink" href="blog/c++/c++静态变量.html">c++静态变量</a></li>
          <li><a class="bloglink" href="blog/c++/c++类型转换.html">c++类型转换</a></li>
          <li><a class="bloglink" href="blog/vim编辑器使用.html">vim编辑器使用</a></li>
          <li><a class="bloglink" href="blog/photos/photos_23_8_6.html">ptohos_23_8_6</a></li>
          <li><a class="bloglink" href="blog/photos/photos_old.html">photos_old</a></li>
          <li><a class="bloglink" href="blog/ubuntu服务器中的lamp架构搭建及配置.html">ubuntu中的lamp架构搭建及配置</a></li>
          <li><a class="bloglink" href="blog/markdown格式说明.html">markdown格式说明</a></li>
          <li><a class="bloglink" href="blog/algorithms/动态规划算法_最长子串.html">动态规划算法_最长子串</a></li>
          <li><a class="bloglink" href="blog/git.html">git&github</a></li>
          <li><a class="bloglink" href="blog/algorithms/贪心算法.html">贪心算法</a></li>
      </ol>
      </div>
  </template>
  <script setup>
  </script>
  
  <style scoped>
  /*blog列表*/
  /* 未访问链接的样式 */
  /* .content{
      width: 100%;
      height: 90vh;
      background-color: #0f0;
  } */
  #blog_list a { 
      color: #333; /* 设置链接文字颜色 */
      text-decoration: none; /* 去掉默认的下划线 */
      }
  
  /* 鼠标悬停链接的样式 */
  #blog_list a:hover {
      color: #333; /* 设置链接文字颜色 */
      text-decoration: underline; /* 添加下划线 */
      cursor: pointer;/*设置手型图标*/
  }
  </style>