## 哈希表
unordered_set<元素类型> 表名
### 插入操作
max.insert()
### 查找操作
while(max.find(查找元素)!=max.end())
### 删除元素
max.erase()

## 表达式的左值和右值
当一个对象被用作右值时，使用的是对象的值（内容）  
当一个对象被用作左值时，使用的是对象的身份（在内存中的位置）

## 逻辑运算符的短路求值
逻辑与和逻辑或运算都是先求左侧对象，只有当左侧对象无法单独决定该表达式的结果时，才会去求右侧对象。

## 迭代器方法
```c++
std::vector<std::string> text;
// 假设已经将一些字符串添加到了text向量中

for (std::vector<std::string>::iterator it = text.begin(); it != text.end(); ++it) {
    std::string s = *it;  // 创建字符串副本
    std::cout << s;
}
```

## 在for循环迭代中使用引用来节省内存空间
```c++
vector<string> text;
for(const auto &s: text){
  cout<<s;
}
```

s会直接访问text中每一个string所在内存区域，而不会开辟新的内存区域。

## 赋值运算（=）
* 赋值运算的返回结果时它的左侧运算对象，且是一个左值。类型也就是左侧对象的类型。  
* 如果赋值运算的左右侧运算对象类型不同，则右侧运算对象将转换成左侧运算对象的类型。  
* 赋值运算符满足右结合律，这点和其他二元运算符不一样。 ival = jval = 0;等价于ival = (jval = 0);  


## 混用解引用和递增运算符

`*iter++`等价于`*(iter++)`，递增优先级较高

```c++
auto iter = vi.begin();
while (iter!=vi.end()&&*iter>=0)
	cout<<*iter++<<endl;	// 输出当前值，指针向前移1
```

## 条件运算符（？：）
例：cond? expr1: expr2

## 位运算符
作用于整数类型
*二进制位向左移（<<）或者向右移（>>），移出边界外的位就被舍弃掉了。
*位取反（~）（逐位求反）、与（&）、或（|）、异或（^）
*有符号数负值可能移位后变号，所以强烈建议位运算符仅用于无符号数。

## sizeof运算符和.size()方法
* sizeof(a)是一个运算符，返回一个对象所占的字节数
* a.size()方法可以返回一个容器的元素数量

## 逗号运算符
用于在一个表达式中顺序执行多个子表达式，并返回最后一个子表达式的值。
```c++
int x = 0, y = 0;
int result = (x = 5, y = 10, x + y);  // 这里x和y都被赋值，result将是x+y的值，也就是15
```


## 面向对象
### 基类
* 完整的基类结构
```c++
#include <iostream>

class MyClass {
private:
    int value;

public:
    MyClass(int val) : value(val) {}

    void display() const;
};

// 在类外部初始化成员函数
void MyClass::display() const {
    std::cout << "Value: " << value << std::endl;
}

int main() {
    MyClass obj(42);
    obj.display(); // 输出: Value: 42

    return 0;
}
```

* 基类用virtual实现函数的多态。（模糊）
```c++
class Base {
public:
    virtual void show() {
        cout << "Base class" << endl;
    }
};

class Derived : public Base {
public:
    void show() override {
        cout << "Derived class" << endl;
    }
};

int main() {
    Base* basePtr = new Derived; // 创建一个基类指针，指向派生类对象
    basePtr->show(); // 调用的是派生类的函数，因为show在基类中是虚函数

    delete basePtr;
    return 0;
}
```

### 派生类
* 定义派生类: class Bulk_quote : public Quote{};
* 构造函数和析构函数：派生类一般调用基类的构造函数和析构函数
```c++
class Base {
public:
    Base(int val) {
        // 构造基类部分
    }
};

class Derived : public Base {
public:
    Derived(int val, int derivedVal) : Base(val) {
        // 构造派生类部分
    }
};
```
```c++
class Base {
public:
    virtual ~Base() {
        // 基类析构逻辑
    }
};

class Derived : public Base {
public:
    ~Derived() {
        // 派生类析构逻辑
    }
};
```