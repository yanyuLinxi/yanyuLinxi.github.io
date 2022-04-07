---
title: "Python命名规范"
date: 2021-10-12T10:37:40+08:00
tags : [
   "python相关库学习",
]
categories : [
   "学习"
]
series : []
aliases : []
draft: false
---

从大到小

| 从大到小 |                       命名规范                       |            样例             |
| :------- | :--------------------------------------------------: | :-------------------------: |
| 包名     |                        全小写                        |           sklearn           |
| 模块名   |                  全小写，下划线分割                  |   sklearn.model_selection   |
| 类名     |           首字母大写、驼峰(类名不加下划线)           | ThisIsMyClass, TruncatedSVD |
| 函数名   |              全小写、用下划线增加可读性              |      read_pickle_file       |
| 变量名   | 全小写、用下划线增加可读性（函数名和变量名不可区分） |         my_variable         |
| 常量名   |              全大写、用下划线增加可读性              |       COUNTER_NUMBER        |