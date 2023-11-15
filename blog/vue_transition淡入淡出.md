## transition实现淡入淡出动画
```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Vue 测试实例 - 菜鸟教程(runoob.com)</title>
<script src="https://cdn.staticfile.org/vue/2.2.2/vue.min.js"></script>
<style>
/* 可以设置不同的进入和离开动画 */
/* 设置持续时间和动画函数 */
.fade-enter-active, .fade-leave-active {
    transition: opacity 2s
}
.fade-enter, .fade-leave-to /* .fade-leave-active, 2.1.8 版本以下 */ {
    opacity: 0
}
</style>
</head>
<body>
<div id = "databinding">
<button v-on:click = "show = !show">点我</button>
<transition-group name = "fade">
    <div>
    <p v-show = "show" v-bind:style = "styleobj">动画实例</p>
    <p v-show = "show" v-bind:style = "styleobj">动画实例</p>
    </div>
</transition-group>
</div>
<script type = "text/javascript">
var vm = new Vue({
el: '#databinding',
    data: {
        show:true,
        styleobj :{
            fontSize:'30px',
            color:'red'
        }
    },
    methods : {
    }
});
</script>
</body>
</html>
```
* <transition>标签中只能有一个容器，且应该含有v-if或v-show属性。