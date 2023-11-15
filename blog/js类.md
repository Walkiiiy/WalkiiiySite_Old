## js类
类是用于创建对象的模板
### 创建类
```js
class Runoob {
  constructor(name, url) {
    this.name = name;
    this.url = url;
  }
}
```
在创建对象时会自动调用构造函数constructor()

### 创建对象
* 使用new关键字，创建对象
```js
let site = new Runoob("菜鸟教程",  "https://www.runoob.com");
```
* 使用匿名构造方法（类表达式）
```js
let Runoob = class {
  constructor(name, url) {
    this.name = name;
    this.url = url;
  }
};
console.log(Runoob.name);
// output: "Runoob"
```
在匿名构造中会将方法的名称自动复制给name属性

### 类的方法
```js
class ClassName {
  constructor() { ... }
  method_1() { ... }
}
```
调用时：let obj=new Classname；obj.method();
