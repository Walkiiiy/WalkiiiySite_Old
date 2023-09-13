<template>
    <Navbar/>
    <!--works-->
    <h2>Walkiiiy's works</h2>
    <ol id="blog_list">
    </ol>
    <Footer/>
</template>
<script setup>
import Navbar from '@/components/navbar.vue'
import Footer from '@/components/footer.vue'
</script>
<style>
/* 未访问链接的样式 */
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