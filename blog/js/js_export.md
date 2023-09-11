## js_export
将模块中的变量、函数、类或对象导出，以便其他模块可以导入并使用它们的关键字，通过使用export,import关键字，可以模块化使用js。导出导入方式有两种。
* 命名导出：  
```js
// 在一个模块中导出多个变量和函数
export const myVariable = 42;
export function myFunction() {
  // 函数定义
}

// 在另一个模块中导入
import { myVariable, myFunction } from './myModule';
```
导出多个模块

* 默认导出：
```js
// 在一个模块中默认导出一个类
export default class MyClass {
  // 类定义
}

// 在另一个模块中导入并命名为任何名称
import SomeName from './myModule';
```
默认模块，即主要模块
