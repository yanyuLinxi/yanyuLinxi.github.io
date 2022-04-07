---
title: "Numpy学习笔记"
date: 2021-09-29T08:31:57+08:00
tags : [
   "python相关库学习",
   "机器学习相关库",
]
categories : [
   "学习"
]
series : []
aliases : []
draft: false
---

# API

## 创建数组

1. numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
   1. np.linspace(2.0, 3.0, num=5)
   2. output => array([2.  , 2.25, 2.5 , 2.75, 3.  ])
2. np.random
   1. random.rand(d0, d1, ..., dn)  d为size
   2. np.random.randn(d0, d1, ..., dn)
      1. Return a sample (or samples) from the “standard normal” distribution.
   3. random.randint(low, high=None, size=None, dtype=int)
      1. np.random.randint([1, 5, 7], 10)  多个下限，一个上限。

## 数组操作

1. np.newaxis 功能上等同于 np.expand_dims
   1. a.shape 2, 3
   2. print(np.expand_dims(a, 2).shape) => (2, 3, 1)
   3. print(a[:, :, np.newaxis].shape) => (2, 3, 1)
2. a = ndarry, b=ndarry
   1. a[b] = 在a中用坐标b去取值。即a[[1,2,3,4]]这样子
3. np.tile。对数组进行横向、纵向的复制。

## 判断操作

1. numpy.all(a, axis=None, out=None, keepdims=<no value>, *, where=<no value>)
   1. Test whether all array elements along a given axis evaluate to True.
   2. example: np.all(y == y_pred)
2. numpy.any(a, axis=None, out=None, keepdims=<no value>, *, where=<no value>)
   1. Test whether any array element along a given axis evaluates to True.


## 计算操作
1. np.log()取自然对数。
2. array.std(1)计算第一维的标准偏差standard deviation
3. array.mean(1)求第一维的均值。
4. value_counts()检查数据。
5. 