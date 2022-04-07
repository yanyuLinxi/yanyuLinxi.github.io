---
title: "Scala学习"
date: 2022-01-06T11:37:01+08:00
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
# scala学习网站
https://www.w3cschool.cn/scala/scala-index.html

专为spark学习：https://www.bilibili.com/video/BV1oJ411m7z3?p=11


基础知识
1. 变量var常量val。常量不可修改，常量相当于final 引用。常量指向的对象仍然可以修改。   
   1. val可以不初始赋值。这种情况需要制定变量类型。
   2. 设置val的初衷就是为了保证它可控。
2. 数组：
   1. 数组取值 data(6)：取第7个值。
   2. Nil空集合。
   3. array.mkString(",")将array中的值通过,组合起来。相当于python的string.join。
   4. List.tail 数组的尾部。除开第一个值。List(1,2,3,4).tail=[2,3,4]
   5. List.init 不包含尾部元素
3. 迭代器
   1. iter
      1. 数组转迭代器: list.iterator
   2. API
      1. 最大值。max。 iter.max
4. 模式匹配
   1. data match{ case a:List[_]=>List case dat=>dat}
   2. case后面跟一个对象，可以指定对象的类型用来匹配。
5. 函数定义
   1. 无参函数。当一个函数无需输入参数时，我们称这个函数为“0参函数“。
      1. 如果你在定义0参函数时加了括号，则在调用时可以加括号或者省略括号；
      2. 但当你在定义0参函数时没加括号，则在调用时不能加括号，只能使用函数名。
      3. 调用无参数函数时，可以省略括号。
6. implicit隐式类型。可以通过隐式转换获取一个对象。

符号语法糖：
1. https://www.zybuluo.com/boothsun/note/1014438
2. $符号和python中的fstring一样。放在字符串前引用变量。s"asd ${variable}"就是取variable的值。
3. 匿名函数：
   1. 初始: (num:Int)=>{num*2}
   2. 进阶：自简原则（能简单则简单）
      1. 逻辑代码只有一行，花括号省略: (num:Int)=>num*2
      2. 类型能够推断，类型省略：(num)=>num*2
      3. 如果参数只有一个，小括号可以省略：num=>num*2
      4. 参数只出现一次，且和参数顺序保持一致，使用下划线代替: _*2
   3. 如果有多行，多行语句用分号隔开。
4. tuple _._n表示取第n个值。n下标从1开始。


语法：
1. 1 until 10: [1,10)
2. for(i<- 1 until 10)
3. 自定义函数
   1. def funName(para1:Type1,para2:Type2):Type = { do some things }
   2. Scala函数可以没有return 语句，默认返回最后一个值。
   3. 如果函数的参数在函数体内只出现一次，则可以使用下划线代替
      1. def mul=(_:Int)*(_:Int)
   4. 最后一个参数后加上*，则允许参数重复如def prints(args:String*)
   5. arg<- args 是说对args中的每个 item遍历。
   6. 可以将一个函数赋值给一个变量，
      1. val 变量名 = 函数名+空格+_
      2. 这里函数名后面必须要有空格，表明是函数的原型
   7. 匿名函数格式：
      1. val 变量名 = （参数：类型） => 函数体
   8. 高阶函数：
      1. 高阶函数其实就是普通函数中的参数进一步推广了，高阶函数的参数可以是一个函数，参数名就是函数名，
      2. def valueFor(f:(Double)=>Double,value:Double)=f(value)
         1. f:(Double)=>Double 就是输入的类型，输出的类型。
   9. 柯里化：柯里化函数是将原来接手两个参数的函数转变成新的接收一个参数的函数过程。def mul(x:Int)=(y:Int)=>x*y。 mul(2)(3)
4. 导入包：
   1. import scala.math._
   2. _ 是通配符。等于*