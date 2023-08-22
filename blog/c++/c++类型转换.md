## c++类型转换

### 隐式类型转换
编译器自动完成，无需显示指定。在运算过程中，涉及不同数据类型的操作数。编译器会自动将其中一个操作数转换为更高精度的数据类型，以确保运算的正确性。包括将非布尔类型转换为布尔类型。
### 显示类型转换方法（强制类型转换）
* static_cast：任何明确定义的类型转换，只要不包含底层const，都可以使用。
* dynamic_cast：支持运行时类型识别。
* const_cast：只能改变运算对象的底层const，一般可用于去除const性质。
* reinterpret_cast：通常为运算对象的位模式提供低层次上的重新解释。
```c++
int num = 10;
double d = static_cast<double>(num);  // 使用static_cast将int转换为double

const int* ptr = &num;
int* mutablePtr = const_cast<int*>(ptr);  // 使用const_cast移除const属性

class Base {};
class Derived : public Base {};

Base* basePtr = new Derived();
Derived* derivedPtr = dynamic_cast<Derived*>(basePtr);  // 使用dynamic_cast进行派生类向基类的转换
if (derivedPtr) {
    // 成功转换
}

int intValue = 42;
void* voidPtr = reinterpret_cast<void*>(&intValue);  // 使用reinterpret_cast进行底层位模式转换
```
