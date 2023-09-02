## js_window对象

### 确定浏览窗口尺寸
* var w=window.innerWidth
* var h=window.innerHeight


### window location 获取和修改页面url
* 确定url：document.write(location.href);
* 确定文件路径：document.write(location.pathname);
* 使用window location assign方法加载新的文档(即跳转页面)
```js
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
<script>
function newDoc(){
    window.location.assign("https://www.runoob.com")
}
</script>
</head>
<body>
<input type="button" value="加载新文档" onclick="newDoc()">
</body>
</html>
```

### window histroy 浏览记录前进后退
* history.back() - 与在浏览器点击后退按钮相同
* history.forward() - 与在浏览器中点击向前按钮相同
* 还可以使用histroy.go方法实现同样的功能
    *history.go(1);  // go() 里面的参数表示跳转页面的个数
    history.go(-1)；
    histroy.go(0)//刷新页面

### window navigator 获取用户信息
```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
	
<div id="example"></div>
<script>
txt = "<p>浏览器代号: " + navigator.appCodeName + "</p>";
txt+= "<p>浏览器名称: " + navigator.appName + "</p>";
txt+= "<p>浏览器版本: " + navigator.appVersion + "</p>";
txt+= "<p>启用Cookies: " + navigator.cookieEnabled + "</p>";
txt+= "<p>硬件平台: " + navigator.platform + "</p>";
txt+= "<p>用户代理: " + navigator.userAgent + "</p>";
txt+= "<p>用户代理语言: " + navigator.language + "</p>";
document.getElementById("example").innerHTML=txt;
</script>

</body>
</html>
```
### window 弹窗
* alert 警告框：window.alert("sometext");
* confirm 确认框 ：
```js
var r=confirm("按下按钮");
if (r==true)
{
    x="你按下了\"确定\"按钮!";
}
else
{
    x="你按下了\"取消\"按钮!";
}
```
* prompt 提示框（输入）：
```js
var person=prompt("请输入你的名字","Harry Potter");
if (person!=null && person!="")
{
    x="你好 " + person + "! 今天感觉如何?";
    document.getElementById("demo").innerHTML=x;
}
```