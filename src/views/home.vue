<template>
    <div style="height: 190vh;">
    <div class="compelete_center">
        <h1>Hello :)</h1>
    </div>
    <div style="height: 20vh;"></div>
    <div class="card-group center" style="--card-width:700px; color: black;">
    <div class="box card" style="background-color:rgba(255, 255, 255, 0.75);">
            <p class="tit">一个简单的自我介绍</p>
            <p class="body">
                废柴大学生，专攻各种摆烂和逃课大法。喜欢打mc和瓦罗兰特，也喜欢做项目写前端（bushi）。如果你看到我的works界面是空的，大概是因为啥也不会，根本没有拿得出手的玩意（笑）。另外欢迎来github上骂我：<a href="https://github.com/Walkiiiy" style="color:darkgoldenrod;">一个普通的链接（不是瑟瑟小网站）</a>
            </p>
            <p class="body">
                Idiot piece of shit,dont know nothing,can't do nothing,an absolote failure.Everyone is welcomed to insult me in my github:<a href="https://github.com/Walkiiiy" style="color:darkgoldenrod">a normal link(not pornhub)</a>
            </p>
    </div>
    </div>
    </div>
</template>
<script setup>
</script>
<style scoped>
/* @import url(../tapple/main.css); */

/* 首页将文字居中显示 */
.compelete_center {
    display: flex; /* 使用 Flexbox 布局 */
    justify-content: center; /* 在主轴上居中对齐 */
    align-items: center; /* 在交叉轴上居中对齐 */
    height: 90vh; /* 设置容器高度为视口高度的 100%，这样内容会居中显示在屏幕中间 */
    line-height: 1.7; /*行距*/
}

.compelete_center h1{
    font-size:xx-large;
}
</style>