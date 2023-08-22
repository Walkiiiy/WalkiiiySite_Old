## 静态变量
静态变量在类或函数的内部创建，在类或函数初始化时就分配内存，但是并不会随类或函数的调用完毕而被清除。  
即：所有的同类型函数或类，共用一个静态变量。
* 静态局部变量：定义在函数内部，跨函数生命周期。
```c++
#include <iostream>

void foo() {
    static int counter = 0;  // 静态局部变量
    counter++;
    std::cout << "foo has been called " << counter << " times." << std::endl;
}

int main() {
    foo();
    foo();
    foo();

    return 0;
}
```
* 静态环境变量：属于类，而不是属于对象，在所有对象之间共享，且可以在类的定义外部初始化。
```c++
class MyClass {
public:
    static int staticVar;  // 静态成员变量声明
};

int MyClass::staticVar = 0;  // 静态成员变量初始化

int main() {
    MyClass obj1;
    MyClass obj2;

    obj1.staticVar = 5;
    std::cout << "obj2.staticVar: " << obj2.staticVar << std::endl;  // 输出为5

    obj2.staticVar = 10;
    std::cout << "obj1.staticVar: " << obj1.staticVar << std::endl;  // 输出为10

    return 0;
}
```

* 静态成员函数：针对类本身进行操作，而不是针对某个对象，调用时直接用类名。