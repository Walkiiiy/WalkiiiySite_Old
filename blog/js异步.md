## js 异步函数
创建一个子线程，在内部执行异步操作，同时主线程继续执行。
* 回调函数
* Promise
```js
new Promise(function (resolve, reject) {//参数名称不固定，第一个为成功时将参数传递给then的函数，第二个为失败时将参数传递给cath的函数
    var a = 0;
    var b = 1;
    if (b == 0) reject("Divide zero");
    else resolve(a / b);
}).then(function (value) {
    console.log("a / b = " + value);
}).catch(function (err) {
    console.log(err);
}).finally(function () {
    console.log("End");
});
```
* 异步函数async
使用async函数也可以达到类似的效果：
```js
async function asyncFunc() {
    await print(1000, "First");//阻塞直到完成
    await print(4000, "Second");
    await print(3000, "Third");
}
asyncFunc();
```