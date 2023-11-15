### vue学习：简单notebook实现
实践vue，javascript，css，html，实现基本的notebook功能。
```html
<!DOCTYPE html>
<html>
    <head>
        <title>
            记事本
        </title>
        <!-- css部分：
            .表示挂载类，#表示挂载id，无前缀表示挂载标签名
            background-color背景色
            背景图片示例：
            body
            {
            background-image:url('img_tree.png'); 
            background-repeat:no-repeat; 图像不平铺
            background-repeat:repeat-x; 图像水平平铺
            background-position:right top;图像位置
            }


            color文字颜色
            text-align文字水平对齐方式
            text-decoration 设置文本装饰，主要使用none来删除链接下划线
            text-indent:50px  指定文本首行缩进
            text-transform 转换文大小写
            direction 文字方向
            letter-spacing 字符间距
            line-height 行高（以百分比设置）
            word-spacing 字间距（单词之间)


            font-family:"Times New Roman", Times, serif;设置字体
            font-style 设置字体样式（斜体）
            font-size 设置字体大小（像素值，large，small，百分比等）
            font-weight 指定字体的粗细


            a:link {color:#000000;}      /* 未访问链接*/
            a:visited {color:#00FF00;}  /* 已访问链接 */
            a:hover {color:#FF00FF;}  /* 鼠标移动到链接上 */
            a:active {color:#0000FF;}  /* 鼠标点击时 */

            list-style-type 设置列表项
            list-style-image 设置图片为列表项

            边框样式:
            border-style:设置边框颜色样式
            margin-（left）:设置外边距
            border-color:设置边框颜色
            使用简写可以按照上右下左逆时针顺序依次定义每一条边框
            

        -->
        <style>
            body{
                background-color: rgb(255, 237, 215);
            }
            .todo{background-color:rgba(142, 245, 193, 0.863);
                color: rgb(0, 0, 0);
                text-align:justify;
            }
            .header{
                background-color:navajowhite;
                margin-left: 100px;
                margin-right: 100px;
                margin-bottom: 5px;
                text-align: center;
                border-style: ridge;
                border-width: light;
                border-color:black;
                border-radius: 15px;
            }
            ul{
                margin-left: 50px;
                margin-right: 50px;
                border-width:light;
                border-radius: 15px;
            }
        </style>
    </head>
    <body>
        <section id="app">
        <header class="header" >
            <h1>记事本</h1>
            <input v-model="todoname" placeholder="请输入事项：" class="new_todo">
            <button class="add" @click="add">添加</button>
        </header>
        
        
        <section class="main">
            <ul class="todo"  v-for="(item,index) in list">
                <div class="view">
                    <span class="index">{{index+1}}</span> <label>{{item.name}}</label>
                    <button @click="del(item.id)" class="destroy">删除</button>
                </div>
            </ul>
        </section>
        </section>

        
        <script src="https://cdn.jsdelivr.net/npm/vue@2.7.14/dist/vue.js"></script>
        <script>
            const app =new Vue({
                el:'#app',//挂载点，指明使用vue的对象
                data:{//所有的vue变量声明和初始化
                    todoname:"",
                    list:[]
                },
                methods:{
                    del(id){
                        this.list=this.list.filter(item => item.id !== id)//单行箭头函数，item为参数
                    },
                    add(){
                        if(this.todoname.trim()===''){//.trim()方法去除字符串两端的空格
                            alert('invalid input!')
                            return 
                        }//检验输入是否为空
                        this.list.unshift({//unshift方法，在数组前端插入
                            id:+new Date(),
                            name:this.todoname
                        })
                        this.todoname=''//添加事项后重置输入框内字符串
                    }
                }
            })
        </script>
    </body>
</html>
```