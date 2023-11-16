<template>
<div id="blog_content"></div>
</template>
<script>
import axios from 'axios';
export default{
    data(){
        return {
            mark:'',
        }
    },
    methods:{
        async get_markdown(blog_path){ //向后端发起请求，读取md文档转化为html返回给前端
            // 定义 IP 地址和端口号
            const ipAddress = '127.0.0.1';
            const port = '3000';
            // 拼接完整的 URL
            const apiUrl = `http://${ipAddress}:${port}/blog_content?path=${blog_path}`;
            
            return new Promise((resolve, reject) => {
            axios.get(apiUrl)
            .then(response => {
                resolve(response.data); // 成功时调用 resolve
                })
            .catch(error => {
                console.error(error);
                reject(error); // 失败时调用 reject
                });
            });
        },
        async show_blog(){
        console.log('show_blog_start');
        var blog_path=this.$route.query.blog_path; //vue路由传参
        console.log('blog_path:',blog_path);
        this.mark=await this.get_markdown(blog_path)
        var blog_content=document.getElementById("blog_content");
        blog_content.innerHTML=this.mark;
        },
    },
    mounted(){ //钩子函数，挂载到dom时执行
        this.show_blog();
    },
    watch:{
        $route(to,from) {
            this.show_blog()
        }
    }
}
</script>
<style>
#blog_content{
    background-color: rgba(255, 255, 255, 0.7);
    color: black;
    font-size: large;
    margin-left: 5vw;
    margin-right: 5vw;
    margin-top: 2vw;
    margin-bottom: 2vw;
    padding: 2vw;
}
</style>