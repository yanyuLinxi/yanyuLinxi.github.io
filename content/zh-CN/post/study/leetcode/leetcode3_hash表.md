---
title: "Leetcode3_hash表"
date: 2021-10-20T15:03:30+08:00
tags : [
   "leetcode学习"
]
categories : [
   "学习"
]
series : []
aliases : []
draft: false
---

# 基础知识

hash将通过hash函数将某个东西转为数值，然后存在哈希表上。这个哈希表可能是数组，也可能是红黑树等等。

如果hashCode的数值大于哈希表了，通常会有操作如取模将值限制在哈希表内。

哈希碰撞仍然不可避免，解决方案：
1. 拉链法。在碰撞的地方建立链表。碰撞发生后依次查找。
2. 线性探测法：碰撞后依次往后寻找空位。需要保证dataSize<hashTableSize.

hash表一般在语言中分为三种：array, set, map

总体来说，有set, multiset, unordered_set这三种。

具体区别参考网址：https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%93%88%E5%B8%8C%E8%A1%A8%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.md

总的来说，set、multiset用的是红黑树。set不允许重复。multiset允许key重复。unordered_set用的是哈希表。key是无序的，也不能重复。

有先使用Unordered_set或者_map，然后有序要求用set、map。要重复则multi_set, multi_map


# 1002 查找常用字符

这是个hash表的问题。它要找重复字符。有一种方法是所有的字符串共用一个hash表。这是统计所有字符串中字符出现的次数

还有一种方法就是每个字符串一个hash表。这是统计该字符串中字符的出现次数

结合具体情况具体分析。