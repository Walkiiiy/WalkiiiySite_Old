<template>
    <div style="height: 94vh;">
    <div class="compelete_center">
        <h1 style="font-size: 6vh;">Hello :)</h1>
    </div>
    </div>
</template>
<script >
</script>
<style scoped>
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