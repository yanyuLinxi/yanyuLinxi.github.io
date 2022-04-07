---
title: "Leetcode1_数组"
date: 2021-09-09T15:05:06+08:00
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

登录
https://zhuanlan.zhihu.com/p/119999079


# 704 二分法搜查数组

这个可以用递归处理的问题，就可以用循环处理。

多思考极端元素时的处理办法。一个元素，两个元素等。

注意处理边界，每次mid都应该根据值得区间减一或者加一。

注意保持区间不变性。就是区间要么一直是左闭右开。要么左闭右闭。
推荐左闭右开。这样是符合大多数编程的习惯的。


# 27 移除元素

这题开始没有意识到是什么类型

往后面写，意识到了是双向指针排序的问题。类似于快排这样的处理。

这里其实一开始的想法挺简单的，而且容易实现，没实现成功的原因就是对极限情况没考虑清楚。其实在极限情况下改一下就行了的。


# 977 有序数组的平方

好好读题，题目给的数组本身就有序，所以有更简单的做法

这里重写了下快速排序。


# 209 长度最小的子数组

读题。读题一定要仔细。

注意循环退出条件。思考极端情况。
思路清楚再动笔。
伪代码尽量贴近原生语言

首先我们创建一个数组，它的第 i 个索引是给定 nums 数组中所有前一个元素及其自身的总和。
然后使用二分搜索搜索满足条件的下标索引。使用空间换时间。这个想法要有。


# 59 螺旋矩阵II

Initialize the matrix with zeros, then walk the spiral path and write the numbers 1 to n*n. Make a right turn when the cell ahead is already non-zero.

def generateMatrix(self, n):
    A = [[0] * n for _ in range(n)]
    i, j, di, dj = 0, 0, 0, 1
    for k in xrange(n*n):
        A[i][j] = k + 1
        if A[(i+di)%n][(j+dj)%n]:
            di, dj = dj, -di
        i += di
        j += dj
    return A
同样的想清楚再动手。别人为什么这么简介。
在思想上多下功夫。动笔时少下功夫。
