<template>
    <ul class="navbar">
        <li>
    <router-link to="/" >home</router-link>
        </li>
        <li>
    <router-link to="/blog" >blog</router-link>
        </li>
        <li>
    <router-link to="/works" >works</router-link>
        </li>
    </ul>
    <ul id="navbar-contact">
    <li>
        <router-link to="/contact">contact</router-link>
    </li>
    </ul>
</template>
<style scoped>
/* 导航栏 */
.navbar {
    list-style-type: none; /* 去除默认的列表样式 */
    color:azure;
    margin: 0;
    padding: 0;
    width: 80vw;
    height: 10vh;
    /*background-color: #a3a3a3; /* 导航栏背景颜色 */
}

.navbar li {
    display: inline-block; /* 将列表项显示为水平排列 */
}

.navbar li a {
    text-decoration: none;
    font-size:large;
    padding: 5px 30px; /* 调整导航项的内边距 */
    color: #333; /* 导航项文字颜色 */
}
#navbar-contact{
    width: 20vw;
    position: absolute;
    top:0;
    right:0;
    list-style-type: none;
    height: 10vh;
}

#navbar-contact li a{
    position: absolute;
    top:0;
    right: 30px;
    font-size:large;
    border: none;
    padding: 0px 0px;
    text-align: right;
    color: #333; /* 导航项文字颜色 */
    text-decoration: none;
}

</style>