## DOM：文档对象模型
### 元素查找
* 通过id查找元素：var x=document.getElementById("intro");
* 通过标签名查找元素：var x=document.getElementById("main");var y=x.getElementsByTagName("p");  
（先查找id为main的元素，然后在其中查找所有标签为p的元素）
* 循环输出元素
```js
var x, i, l;
x = document.getElementsByTagName("*");
l = x.length;
for (i = 0; i < l; i++) {
  document.write(x[i].tagName + "<br>");
}
```
