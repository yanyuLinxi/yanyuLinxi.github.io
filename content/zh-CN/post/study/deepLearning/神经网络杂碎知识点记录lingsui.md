---
title: "神经网络杂碎知识点记录"
date: 2021-10-10T16:30:13+08:00
tags : [

]
categories : [

]
series : []
aliases : []
draft: false
---

# 标准化和归一化
1. 缩放到均值为0，方差为1（Standardization——StandardScaler()）
2. 缩放到0和1之间（Standardization——MinMaxScaler()）
3. 缩放到-1和1之间（Standardization——MaxAbsScaler()）
4. 缩放到0和1之间，保留原始数据的分布（Normalization——Normalizer()）
1就是常说的z-score归一化，2是min-max归一化。
归一化Normalization，只是缩放到0，1
标准化Standardization，缩放到0-1，还改变了方差。所以改变了分布。不一定是正态分布。

Notes:
1. 归一化和标准化的选择差异
   1. 当数据范围有严格要求的时候，使用归一化。不涉及距离度量、协方差计算则归一化。
   2. 标准化更通用，无从下手，则用标准化。数据极端变化用标准化。分类算法、聚类算法是标准化效果更好。



# 二分类一般都是输出一个值。
输出两个值的话，权重量增加了一倍。得不偿失。不用。在结尾层使用sigmoid激活函数。

现在二分类一般都是两个值。

但是如果你是使用交叉熵损失函数的话，那几个分类，就是输出几个值。

# one-hot 的作用和意义

One-hot主要用来编码类别特征，即采用哑变量（dummy variables）对类别进行编码。 它的作用是避免因将类别用数字作为表示而给函数带来抖动。 直接使用数字会将人工误差而导致的假设引入到类别特征中，比如类别之间的大小关系，以及差异关系等等

# TP FP FN TN P recall Accuracy

tp = 预测为正，实际为正
fp = 预测为正，实际为负
fn = 预测为负，实际为正
tn = 预测为负，实际为负

p = tp/(tp+fp)
R = tp/(tp+fn)
acc = (tp+tn)/(tp+tn+fp+fn)