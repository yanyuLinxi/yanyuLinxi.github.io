---
title: "Java重拾"
date: 2022-01-05T15:49:38+08:00
tags : [
   "java学习"
]
categories : [
   "学习"
]
series : []
aliases : []
draft: false
---

基本数据类型：
小数默认double。float数值需要额外添加字母f 
长整型245L

理解：
1. 申明，基本类型申明的是变量，是深度拷贝，类申明的是引用。Hero b; 申明的都是引用。
2. 实例化后，才是对象。123, new Hero()都是实际的占用内存的值。

类：
1. 继承
   1. public class a extends b
   2. 继承会拥有b的属性。
2. 构造函数
   1. public A(){}
3. 类引用，引用的是对象，所以修改对象会修改其他指向这个引用的值。
4. 权限：成员变量有四种修饰符
   private 私有的  仅仅自身访问
   package/friendly/default 不写。 同包继承访问
   protected 受保护的 子类继承访问
   public 公共的 所有人继承访问。
5. 静态类、静态方法。推荐类名访问。所有对象共有。
6. 静态初始化块：
   1. static{初始化各个值。}
   2. 属性声明-》初始化块-》构造方法。按顺序赋值。
7. 单例模式。
   1. 自己申明一个私有静态属性指向自己的对象。
   2. 申明一个静态方法，返回这个对象。
      1. 也可以静态方法时才调用对象。称作懒汉。
      2. 懒汉会有线程安全的问题。初始化时间充分，饿汉。否则懒汉。饿汉当有类存在时即加载。


系统API：
1. Array:
   1. Arrays.copyOfRange(array, start, end)
   2. Arrays.toString()
   3. Arrays.sort(a)
   4. Arrays.binarySearch 二分法。使用前先排序。
   5. Arrays.equals(a,b) 比较两个数组是否相同。
   6. Arrays.fill(a, int) 填充数组。
2. 

其他API：
1. enum 类型。public enum season{day1, day2}。
   1. season.values()所有的枚举。

tips:
1. final类型仅仅可以赋值一次。final可以修饰函数，类。
2. 长路与&，短路与&&。按位与&
3. 有符号右移>> 不带符号右移>>>
4. 一维数组int a[] = new int[]
5. 二维数组int a[][] = new int[2][3]
   1. 或者int a[][] = new int[2]; int a[0] = new int[3]
6. 同个package下的包直接调用，不同package下的包需要import
7. 