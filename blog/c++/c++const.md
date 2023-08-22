##  const

### (1) const 基础

如果const关键字不涉及到指针则很好理解，下面是涉及到指针的情况：

	int b = 500;
	const int* a = &b; [1]
	int const *a = &b; [2]
	int* const a = &b; [3]
	const int* const a = &b; [4]

可以参考《Effective c++》Item21上的做法，
如果 const 位于星号的左侧，则 const 就是用来修饰指针所指向的变量，即指针指向为常量；如果 const 位于星号的右侧，const 就是修饰指针本身，即指针本身是常量。

因此，[1]和[2]的情况相同，都是指针所指向的内容为常量（const放在变量声明符的位置无关），这种情况下不允许对内容进行更改操作，如不能*a = 3；[3]为指针本身是常量，而指针所指向的内容不是常量，这种情况下不能对指针本身进行更改操作，如a++是错误的；[4]为指针本身和指向的内容均为常量。

### (2) 作为参数

	void display(const double& r);
	void display(const double* r);

说明:

1. 在引用或者指针参数的时候使用 const 限制是有意义的，而对于值传递的参数使用 const 则没有意义
2. 保证引用的变量的值不被改变
3. const 在 double 前或者后面意思相同，只是不同的人的写法不同

### (3) const对象

声明为 const 的对象只能访问类中声明为 const 的成员函数，不能调用其它成员函数。

### (4) const成员函数

	类型说明符 函数名(参数表) const;
	void print(int i) const;

说明:

1. const 是函数类型的一个组成部分，因此在实现部分也要带 const 关键字
2. 常成员函数不能更新对象的数据成员，也不能调用该类中没有用 const 修饰的成员函数