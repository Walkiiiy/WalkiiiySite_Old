##javascript数组
```javascript
// 创建一个空数组
let emptyArray = [];

// 创建一个包含一些元素的数组
let fruits = ['apple', 'banana', 'orange'];

// 访问数组元素
console.log(fruits[0]); // 输出: 'apple'
console.log(fruits[1]); // 输出: 'banana'

// 修改数组元素
fruits[1] = 'grape'; // 将第二个元素从 'banana' 改为 'grape'

// 添加元素到数组末尾
fruits.push('pear');

// 删除数组末尾的元素
fruits.pop();

// 获取数组的长度
console.log(fruits.length); // 输出: 3

// 遍历数组元素
for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);
}

// 使用 forEach 遍历数组
fruits.forEach(function(fruit) {
    console.log(fruit);
});

// 使用 map 创建一个新数组
let uppercaseFruits = fruits.map(function(fruit) {
    return fruit.toUpperCase();
});

// 在数组头部添加一个元素
fruits.unshift('apple'); // ['apple', 'banana', 'orange']

// 在数组头部添加多个元素
fruits.unshift('grape', 'kiwi'); // ['grape', 'kiwi', 'apple', 'banana', 'orange']
```