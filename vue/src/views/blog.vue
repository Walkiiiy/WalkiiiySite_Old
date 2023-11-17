<template>
    <!--博客页-->
        <div id="blog_box">
        <h2>Walkiiiy's blog</h2>
        <ol id="blog_list">
            <!-- <li>{{blog_list}}</li> -->
            <!-- <li><router-link :to="{ path: '/blog_read', query: {blog_path:'js数组.md'}}"> js数组 </router-link> </li> -->
            <li v-for="item in blog_list">
                <router-link :to="{ path: '/blog_read', query: {blog_path:item}}">{{ item }}</router-link>
            </li>
        </ol>
        </div>
</template>
<script>
import axios from 'axios';
export default{
    data(){
        return {
            blog_list:{},
        }
    },
    methods:{
        get_blog_list(){
            const ipAddress = '111.231.21.55';
            const port = '3000';
            // 拼接完整的 URL
            const apiUrl = `http://${ipAddress}:${port}/blog_list`;
            axios.get(apiUrl)
            .then(response => {
                console.log('res:', response.data);
                this.blog_list=response.data;
                })
            .catch(error => {
                console.error(error);
                return error;
                });
        }
    },
    mounted(){
        this.get_blog_list();
    }
}
</script>
<style scoped>
  #blog_box{
      background-color:rgba(150,150,150,0.05);
      margin:30px;
      padding-left: 30px;
  }
    #blog_list a { 
        color:azure; /* 设置链接文字颜色 */
        text-decoration: none; /* 去掉默认的下划线 */
      font-size: large;  
      }
    
    /* 鼠标悬停链接的样式 */
    #blog_list a:hover {
        color: #333; /* 设置链接文字颜色 */
        text-decoration: underline; /* 添加下划线 */
        cursor: pointer;/*设置手型图标*/
    }
    
</style>