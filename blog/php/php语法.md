## $argc,$argv
PHP会在脚本运行时根据参数创建两个特殊的变量，$argc是一个整数，表示参数个数，$argv是一个数组变量，包含每个参数的值， 它的第一个元素一直是PHP脚本的名字

## Datetime类

### 获取现在时间
使用 new \Datetime 获取现在的时间对象。

### 字符串和时间对象的转化
使用createFromFormat()方法把时间日期类型的字符串对象转换为时间对象。
```php
$start = \DateTime::createFromFormat('d. m. Y', $raw);
```
小写的y会省略年的前两位。

使用format()方法把时间对象转换为字符串
```php
echo "Start date: " . $start->format('m/d/Y') . "\n";
```

### 时间对象的计算和比较

时间对象之间可以直接比较
```php
<?php
if($start < $end) {
    echo "Start is before end!\n";
}
```

## 基础语法

### 符号
= 赋值
== 比较值
=== 比较类型和值

### 语句
if else 语句和c语言相同  
return 和c语言相同  
switch case 和c语言相同  
```php
switch ($a) {
        case 1:
            // code...
            break;             // break is used to end the switch statement
        case 2:
            // code...         // with no break, comparison will continue to 'case 3'
        case 3:
            // code...
            return $result;    // within a function, 'return' will end the function
        default:
            // code...
            return $error;
}
```

### 函数
fopen()方法和c相同  
```php
//读取普通文件
$fpath=iconv('UTF-8','GB2312',"题库.csv");
$file=fopen($fpath,"r") or exit("无法打开文件!");
//此处省略相关操作
fclose($file);    
```

```php
//读取csv文件
<?php
$fh=fopen("a.csv","r");//这里我们只是读取数据，所以采用只读打开文件流
$arr=fgetcsv($fh);//这个函数就是读取CSV文件的函数，他把文本读入后转为数组存储在$arr中
fclose($fh);
foreach($arr as $key=>$value){echo $value;}//循环输出所有的值
?>
```

## 命名空间
使用'\'指明命名空间，如果前面什么都不加，则默认为global
```php
<?php
namespace phptherightway;

function fopen()
{
    $file = \fopen();    // Our function name is the same as an internal function.
                         // Execute the function from the global space by adding '\'.
}

function array()
{
    $iterator = new \ArrayIterator();    // ArrayIterator is an internal class. Using its name without a backslash
                                         // will attempt to resolve it within your namespace.
}
```
多个命名空间同时存在：
```php
<?php
namespace MyProject {

const CONNECT_OK = 1;
class Connection { /* ... */ }
function connect() { /* ... */  }
}

namespace { // 全局代码
session_start();
$a = MyProject\connect();
echo MyProject\Connection::start();
}
?>
```
注意：命名空间的声明必须是程序的第一条语句
```php
<html>
<?php
namespace MyProject; // 命名空间前出现了“<html>” 会致命错误 -　命名空间必须是程序脚本的第一条语句
?>
```

## 字符串
单引号字符串：速度快，不能做语法转换，可以使用.进行字符串连接。
双引号字符串：可以进行语法转换。
```php
<?php
echo 'phptherightway is ' . $adjective . '.'     // a single quotes example that uses multiple concatenating for
    . "\n"                                       // variables and escaped string
    . 'I love learning' . $code . '!';

vs.

echo "phptherightway is $adjective.\n I love learning $code!"  // Instead of multiple concatenating, double quotes
                                                               // enables us to use a parsable string
```

## 三元运算符
```php
<?php
$a = 5;
echo ($a == 5) ? 'yay' : 'nay';
```