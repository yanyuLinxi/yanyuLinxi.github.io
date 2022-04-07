---
title: "JavaParser学习"
date: 2022-01-10T09:45:33+08:00
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

1. Pretty Printing是用来将AST打印成代码的。
2. NodeText和具体的语法模型
   1. Void foo (int a ){}
   2. Type child: void
   3. Name child: foo
   4. param child: int a
   5. body child: {}
3. TreeVisitor。使用树访问模式来访问一个节点和子节点。
4. 通过getClass()获取节点的类。来判断是不是叶子节点。
5. 直接打印Node node，打印出来的是这个节点和子节点的代码。  
   1. getChildNodes()获取节点子节点。
   2. getData(DataKey)通过DataKey获取节点数据。 不清楚DataKey是什么。