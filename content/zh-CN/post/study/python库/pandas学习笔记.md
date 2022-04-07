---
title: "Pandas学习笔记"
date: 2021-11-24T09:40:51+08:00
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

# 资料
https://github.com/datawhalechina/joyful-pandas

# pandas 临时杂碎知识点记录

1. .null()检测是否有空值
2. .sum()对pandas数值进行求和
3. .unique()检测pandas中的独一值。
4. train_df.info()查看dataframe的信息。
5. train_df.describe(include=['O'])会计算离散变量的统计特征。
6. df.groupby("字段")
   1. 这个操作会返回一个df对象，后续的agg,apply等操作可以基于这个对象进行操作。
7. df.sort_values(by="字段", ascending=False)降序排列。
8. 字符串处理 df.字符串字段.str.extract('正则化语言')
9. df.replace 替换字段值。
10. df.map() 通过字典进行map
11. df.fillna(0)将na 填为0.
12. pd.cut 对数据进行分割。