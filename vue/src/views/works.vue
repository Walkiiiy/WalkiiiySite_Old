<template>
    <!--博客页-->
        <div id="blog_box">
        <h2 style="color: rgb(39, 36, 36); font-size: x-large;">Walkiiiy's works</h2>
        <ol id="blog_list">
            <a src="https://github.com/Walkiiiy/Zensplit"><h3>Zensplit</h3></a>
            <p style="color:rgb(35,35,35);">{{ ZensplitIntro }}</p>
            <a src="https://github.com/Walkiiiy/ProjectSheldon"><h3>ProjetSheldon</h3></a>
            <p style="color:rgb(35,35,35);">{{ ProjectSheldonIntro }}</p>
        </ol>
        </div>
</template>
<script>
export default{
    data(){
        return {
            ZensplitIntro: '一个基于多种方案的字符切割技术，它能返回你的图片中的每一个字符的精准位置',
            ProjectSheldonIntro:'一个论坛，探讨、猜想和预测社会发展的趋势和方向。',
        }
    },
    methods:{
    },
    mounted(){
    }
}
</script>
<style scoped>
#blog_box{
    background-color:rgba(255,255,255,0.7);
    color: black;
    margin:30px;
    padding: 30px;
    height: 80vh;
}
#blog_list li{
    color: black;
    margin: 7px;
}
#blog_list a { 
    color:black; /* 设置链接文字颜色 */
    text-decoration: none; /* 去掉默认的下划线 */
    font-size:larger;
    }

/* 鼠标悬停链接的样式 */
#blog_list a:hover {
    color: #333; /* 设置链接文字颜色 */
    text-decoration: underline; /* 添加下划线 */
    cursor: pointer;/*设置手型图标*/
}

</style>