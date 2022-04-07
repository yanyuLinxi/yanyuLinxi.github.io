---
title: "Deep Learning for Unsupervised Insider Threat Detection in Structured Cybersecurity DataStreams"
date: 2021-09-24T19:33:54+08:00
tags : [
    "论文阅读笔记",
    "异常行为分析",
    "RNN",
]
categories : [
    "论文阅读笔记",
]
series : []
aliases : []
draft: false
math: true
---

# 目录： <!-- omit in toc -->
- [1. 综述翻译](#1-综述翻译)
  - [1.1 发表于](#11-发表于)
- [2. Tag](#2-tag)
- [3. 任务描述](#3-任务描述)
- [4. 方法](#4-方法)
  - [概述](#概述)
  - [细节](#细节)
    - [Feature Extraction](#feature-extraction)
    - [Structured Stream Neural Network](#structured-stream-neural-network)
      - [DNN](#dnn)
    - [RNN](#rnn)
  - [输出](#输出)
  - [内部危害检测：](#内部危害检测)
- [6. 实验结果](#6-实验结果)
- [5. 解决了什么问题（贡献）](#5-解决了什么问题贡献)
- [7. 如何想到该方法](#7-如何想到该方法)
- [8. 我能否想到该方法](#8-我能否想到该方法)
- [9. 创新点是什么](#9-创新点是什么)
- [10. 如何用于本专业](#10-如何用于本专业)
- [11. 该方案还存在的问题](#11-该方案还存在的问题)
- [12. 注释](#12-注释)

# 1. 综述翻译

分析组织的计算机网络活动是早期检测和缓解内部威胁的关键组成部分，这是许多组织日益关注的问题。原始系统日志是流数据的典型示例，可以快速扩展超出人类分析师的认知能力。作为人类分析师的预期过滤器，我们提出了一种在线无监督深度学习方法，以实时检测系统日志中的异常网络活动。我们的模型将异常分数分解为个人用户行为特征的贡献，以提高可解释性，以帮助分析师审查潜在的内部威胁案例。使用 CERT 内部威胁数据集 v6.2 和威胁检测召回作为我们的性能指标，我们新颖的深度和循环神经网络模型优于主成分分析、支持向量机和基于隔离森林的异常检测基线。对于我们的最佳模型，我们数据集中标记为内部威胁活动的事件的平均异常分数为 95.53 个百分点，这表明我们的方法有可能大大减少分析师的工作量。

## 1.1 发表于

aaai 2017

# 2. Tag

Insider Threat; LSTM; unsupervised;

# 3. 任务描述

# 4. 方法

## 概述
我们提出了一个在线无监督深度学习系统来过滤系统日志数据以供分析师审查。 由于内部威胁行为千差万别，我们不会尝试对威胁行为进行明确建模。 相反，深度神经网络 (DNN) 和循环神经网络 (RNN) 的新变体经过训练，可以识别网络上每个用户的特征活动，并同时实时评估用户行为是正常还是异常。 考虑到流媒体场景，我们方法的时间和空间复杂度作为流持续时间的函数是恒定的； 也就是说，不会无限期地缓存任何数据，并且在将新数据输入到我们的 DNN 和 RNN 模型时进行检测。 为了帮助分析师解释系统决策，我们的模型将异常分数分解为人类可读的导致检测到的异常的主要因素的摘要（例如，用户在凌晨 12 点到早上 6 点之间将异常大量的文件复制到可移动媒体）。

图 1 概述了我们的异常检测系统。 

+ 首先，来自系统用户日志的原始事件被输入到我们的特征提取系统中，该系统聚合它们的计数并为每个用户每天输出一个向量。 
+ 然后将用户的特征向量输入神经网络，创建一组网络，每个用户一个。 在我们系统的一种变体中，这些是 DNN； 另一方面，它们是 RNN。 在任何一种情况下，不同的用户模型共享参数，但对于 RNN，它们保持独立的隐藏状态。
+ 这些神经网络的任务是预测序列中的下一个向量； 实际上，他们学会了为用户的“正常”行为建模。 异常与预测误差成正比，有足够的异常行为被标记以供分析师调查。

![图1](/researchPng/research/dllunsupervisedLSTM.png)

## 细节

### Feature Extraction
我们的系统从这些来源中提取了两种信息：分类用户属性特征和连续“计数”特征。

categorical user attribute features分类用户特征是指用户在组织中的角色、部门和主管等属性。有关我们实验中使用的分类特征列表（以及每个类别中不同值的数量），请参见表 1

除了这些分类特征之外，我们还累积了用户在某个固定时间窗口（例如 24 小时）内执行的 408 项“活动”的计数。计算活动的一个示例是下午 12:00到下午 6:00 之间来自可移动媒体的不常见非诱饵文件副本的数量。图 2 直观地列举了一组计数特征：只需沿着一条从右到左的路径，沿途在每个集合中选择一个项目。所有这些遍历的集合是计数特征的集合。对于每个用户 u，对于每个时间段 t，将分类值和活动计数串联起来变成一个414维的数字特征向量xu

414=6+408

### Structured Stream Neural Network
我们系统的核心是两个神经网络模型之一，该模型将给定用户的一系列特征向量（每天一个）映射到用户序列中下一个向量的概率分布。 该模型以在线方式同时对所有用户进行联合训练。 首先，我们描述了我们的 DNN 模型，它没有明确地对任何时间行为进行建模，然后是 RNN，它可以。 然后我们讨论用于预测结构化特征向量和识别特征向量流中的异常的其余部分。

#### DNN

根据前文所说，一共分成了T个时间段。对于每个时间段组成了vectors $x_t^u$, DNN将这些$x_t^u$转为$h_t^u$

### RNN

前面的T个特征值$h_t^u$按顺序送入LSTM。这样当前输入不仅与当前时间段有关，而且和前一个时间段有关。

## 输出

RNN得到的特征$h_{t-1}$用来进行预测。

对于408个统计量counter和6个角色特征C={R,P,F,D,T,S}分别进行预测

> Therefore, the P is actually the joint probability over the counter vector and each of the categorical variables: role (R), project (P), functional unit (F), department (D), team (T) and supervisor (S).

这里使用7个单层隐藏层来得到输出概率：
![math](/researchPng/research/insiderthreatLSTM.png)

对于6个角色属性使用softmax函数进行归一化得到离散概率。
对于counter使用正态分布获取连续概率分布。

> 我们将六个分类变量的条件概率建模为离散的，而我们将计数的条件概率建模为连续的。对于离散模型，我们使用标准方法：类别 k 的概率只是向量 θ(V) 的第 k 个元素，其维度等于类别的数量。例如，有 47 个角色，所以 θ(R) ∈ R47。因为我们使用 softmax 输出激活来产生 θ(V)，所以元素是非负的并且总和为一

> 对于计数向量，我们使用多元正态密度。我们考虑两个变体。第一个，我们的模型输出平均向量 μ (θ(ˆx) = μ)，我们假设协方差 Σ 是恒等式。使用恒等协方差，最大化真实数据的对数似然相当于​​最小化平方误差。在第二个中，我们假设对角协方差，我们的模型输出均值向量和 Σ 对角线的对数。模型的这部分可以看作一个简化的混合密度网络（Bishop 1994）。

文中使用两种预测方式运算。
+ 下一个时间步预测：用本时间步特征预测下一个时间步的值 
+ 同一个时间步预测：用本时间步特征预测本时间步的值。

使用本时间步值的原因：

> An auto-encoder is a parametric function trained to reproduce the input features as output. Its complexity is typically constrained to prevent it from learning the trivial identity function; instead, the network must exploit statistical regularities in the data to achieve low reconstruction error for commonly found patterns, at the expense of high reconstruction error for uncommon patterns (anomalous activity). Networks trained in this unsupervised fashion have been demonstrated to be very effective in several anomaly detection application domains (Markou and Singh 2003).

自动编码器是经过训练的参数函数，用于将输入特征再现为输出。 它的复杂性通常受到限制，以防止它学习琐碎的身份函数； 相反，网络必须利用数据中的统计规律来实现常见模式的低重构误差，但代价是不常见模式（异常活动）的高重构误差。 以这种无监督方式训练的网络已被证明在几个异常检测应用领域非常有效（Markou 和 Singh 2003）。

## 内部危害检测：

我们模型的目标是检测内部威胁。我们假设以下条件：我们的模型产生异常分数，用于从最异常到最少对用户天数进行排名，然后我们将排名最高的用户天对提供给判断异常行为是否表明内部威胁的分析师。我们假设有一个每日预算，它规定了每天可以判断的最大用户日对数，并且如果向分析师呈现内部威胁的实际案例，他或她将正确检测到它。

> One key feature of our model is that the anomaly score decomposes as the sum over the negative log probabilities of our variables; the continuous count random variable further decomposes over the sum of individual feature terms: (xi − µi)/σi. This allows us to identify which features are largest contributors to any anomaly score; 

我们模型的一个关键特征是异常分数分解为我们变量的负对数概率的总和；连续计数随机变量进一步分解单个特征项的总和：(xi − µi)/σi。这使我们能够确定哪些特征对任何异常分数的贡献最大；

为了适应在线场景，我们对标准训练方案进行了重要调整。对于 DNN，主要区别在于每个样本只能观察一次的限制。对于 RNN 来说，情况更为复杂。我们同时训练多个用户序列，每次看到用户的新特征向量时都会反向传播和调整权重。从逻辑上讲，这对应于每个用户训练一个 RNN，其中权重在所有用户之间共享，但隐藏状态序列是每个用户。在实践中，我们通过使用补充数据结构训练单个 RNN 来实现这一点，该结构存储每个用户的过去输入以及隐藏和单元状态的有限窗口。每次将用户的新特征向量输入模型时，在计算前向传播和反向传播误差时，该用户的隐藏状态和单元状态将用于上下文。

简单点讲，每个用户拥有自己的时间序列。



# 6. 实验结果

训练和测试时，仅训练和测试了工作日，将周末分开了。因为工作日和周末的正常情况在性质上是不同的。如果需要，可以训练第二个系统模拟正常的周末行为。

测试显示，当前时间步预测比下一个时间步预测效果要稍微更好点。
![result](/researchPng/research/insiderthreatLSTMResult.png)

 Cumulative Recall 累计召回率。
 precision 衡量查准率。召回率衡量查全率。

![result](/researchPng/research/insiderthreatLSTMResult-2.png)
我们进行了两次分析以更好地理解我们系统的行为，使用我们最好的 DNN 模型来说明。首先，我们看看时间对模型异常概念的影响。由于模型开始时完全未经训练，所有用户的异常分数在最初几天都非常高。当模型看到用户行为的例子时，它很快就会知道什么是“正常”。图 4 显示了作为天函数的异常（在前几天的“老化”期之后开始，以保​​持 y 轴刻度易于管理）。百分比范围显示（根据当天的用户计算），恶意（内部威胁）用户天覆盖为红点。请注意，所有恶意事件都高于异常的第 50 个百分位，大多数都高于第 95 个百分位。

![result](/researchPng/research/insiderthreatLSTMResult-3.png)
在我们的第二个分析中，我们研究了每日预算的影响
关于最佳 DNN、最佳 LSTM 和三个基线模型的回忆。图 5 绘制了这些召回曲线。令人印象深刻的是，在每日预算为 425 的情况下，DNN-Diag、LSTM-Diag 和隔离森林模型都获得了 100% 的召回率。它还表明，使用我们的 LSTM-Diag 系统，只需 250 的预算即可获得 90% 的召回率（分析师需要考虑的数据量减少了 93.5%）。

# 5. 解决了什么问题（贡献）

我们的模型试图解决将机器学习应用于网络安全领域（Sommer and Paxson 2010）的几个关键困难。
1. 网络上的用户活动在几秒到几小时内通常是不可预测的，这导致难以找到“正常”行为的稳定模型。我们的模型以在线方式持续训练，以适应数据中不断变化的模式。
2. 此外，恶意事件的异常检测尤其具有挑战性，因为攻击者经常试图密切模仿典型行为。我们将系统日志流建模为具有用户元数据的交错用户序列，以便为网络上的活动提供精确的上下文；例如，这允许我们的模型识别用户、同一角色的员工、同一项目团队的员工等的真正典型行为。 
3. 我们评估我们的模型在合成 CERT Insider Threat v6.2 上的有效性数据集（Lindauer et al. 2014；Glasser and Lindauer 2013），其中包括带有内部威胁活动行级注释的系统日志。真实威胁标签仅用于评估。

# 7. 如何想到该方法

# 8. 我能否想到该方法

# 9. 创新点是什么

# 10. 如何用于本专业

# 11. 该方案还存在的问题

# 12. 注释
