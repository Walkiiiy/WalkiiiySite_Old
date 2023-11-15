## vue.js与vite_工程化配置
基于ubuntu22.04系统，官方文档：https://cn.vuejs.org/guide/quick-start.html
#### 构建vue项目
npm create vue@latest
### 关于vite
使用esm模块化标准开发极大丰富了前端页面的可能性（搭配包管理工具npm，yarn），但是会遇到问题：
* 部署后访问页面，因组件过多而加载缓慢
* 浏览器对不同模块的兼容性问题 
为了解决以上问题，产生了包管理器，如webpack，vite   
vite相较于webpack运行速度显著提高。
### 在npm构建的vue项目内使用vite
* 默认的文件解析地址即为根目录，也可以自行构建子目录src
* npm run dev 运行调试。   
  开发调试时vite不会对文件进行打包，而且会针对文件的更改对页面进行动态更新。
* npm run build 打包，保存在dist目录下。   
   
tip：初始化后只有.gitignore文件，git需要自行初始化