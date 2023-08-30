## js对象和方法
```js
<p id="demo"></p> 
<script>
var person = { //定义一个对象，赋值给变量容器
    firstName: "John", //对象的属性
    lastName : "Doe",
    id : 5566,
    fullName : function()  对象的方法
	{
       return this.firstName + " " + this.lastName;
    }
};
document.getElementById("demo").innerHTML = person.fullName();
</script>
```
### 方法的多种定义形式
* 函数表达式：myMethod: function(){}  
  简写形式： myMethod() {}
* 箭头函数： myMethod: () => {}
* 将函数赋值给方法：
```js
function myFunction() {}
const myObject(){
    mtMethod: myFunction
};
```
* 使用类：用包含方法的类定义对象，然后调用该对象的方法。