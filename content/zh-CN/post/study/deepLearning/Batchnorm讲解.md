---
title: "Batchnorm讲解"
date: 2021-11-22T20:25:16+08:00
tags : [

]
categories : [

]
series : []
aliases : []
draft: false
---

# 引用

https://mp.weixin.qq.com/s/QFpolIXvOQjUsPAngqvqmg

论文：
Correct Normalization Matters: Understanding the Effect of Normalization On Deep Neural Network Models For Click-Through Rate Prediction：https://arxiv.org/pdf/2006.12753.pdf

# 介绍

**谷歌**在2015年就提出了**Batch Normalization(BN)**，该方法对每个mini-batch都进行normalize，会把mini-batch中的数据正规化到均值为0，标准差为1，同时**还引入了两个可以学的参数**，分别为scale和shift，让模型学习其适合的分布。

**那么为什么在做过正规化后，又要scale和shift呢？**
因为scale和shift是模型自动学习的，神经网络可以自己琢磨前面的正规化有没有起到优化作用，没有的话就"反"正规化，抵消之前的正规化操作带来的影响。

让特征分布有一定的自由度，可以调整到对下一层更好的分布。

BatchNormalization是对一批样本进行处理, 对一批样本的每个特征分别进行归一化

**LayerNormalization**是对一个样本进行处理，对一个样本的所有特征进行归一化，乍一看很没有道理，因为如果对身高体重和年龄一起求一个均值方差，都不知道这些值有什么含义，但存在一些场景却非常有效果——**NLP领域**。 在NLP中，N个特征都可能表示不同的词，这个时候我们仍然采用BatchNormalization的话，对第一个词进行操作，很显然意义就不是非常大了，因为任何一个词都可以放在第一个位置，而且很多时候词序对于我们对于句子的影响没那么大，而此时我们对N个词进行Normalization等操作可以很好地反映句子的分布。(LN一般用在第三维度，[batchsize, seq_len,dims])，因为该维度特征的量纲是相同的，所以并没有太多区别。

# 为什么要用Normalization？
1. 解决梯度消失
拿sigmoid激活函数距离，从图中，我们很容易知道，数据值越靠近0梯度越大，越远离0梯度越接近0，**我们通过BN改变数据分布到0附近**，从而解决梯度消失问题。

2. 解决了ICS internal Covariate Shift. 
由于训练过程中参数的变化，每一层的更新，导致上层的输入数据分布发生巨大变化，每一次高层需要重新学习去适应新的分布。神经网络就要学习**新的分布**，随着层数的加深，学习过程就变的愈加困难，**要解决这个问题需要使用较低的学习率，由此又产生收敛速度慢**，因此引入BN可以很有效的解决这个问题。数据分布变化很大

3. 加速了模型收敛速度。

和对原始特征做归一化类似，BN使得每一维数据对结果的影响是相同的，由此就能加速模型的收敛速度。

4. 引入了部分噪声。提升了泛化能力。

# 解析
我们发现 Normalization有效的最大一个原因在于方差的影响而不是均值。

## 特征Embedding上加入Normalization是否有效？
从上面的实验中,我们发现,在特征Embedding层加入Normalization都是有效的,而且LayerNorm以及相关的变种是效果相对稳定以及最好的;


## normalization公式：
$\frac{x-\mu}{\theta}$, $\theta$是标准差。减去平均值除以标准差。

$$y = \frac { x - E [ x ] } { \sqrt {Var [ x ] + \xi } } * \gamma + \beta$$

## 问题：
1. Batch Norm的描述：
   1. 该方法对每个mini-batch都进行normalize，会把mini-batch中的数据正规化到均值为0，标准差为1，同时还引入了两个可以学的参数，分别为scale和shift，让模型学习其适合的分布。
2. Normalization的优点：
   1. 四条：
      1. 梯度消失
      2. 加快网络训练
      3. 引入噪声，提高泛化
      4. 解决ICS（内部协变量偏移问题）
         1. 为什么引入噪声能提升泛化？加入噪声可以认为是在增加网络训练的难度，可以达到一定的正则效果。提升模型的鲁棒能力。
   2. 缺点：1. 当Batch小的时候，均值和方差不稳定
3. 和归一化的不同
   1. BatchNormalization层和正规化/归一化不同，BatchNormalization层是在mini-batch中计算均值方差，因此会带来一些较小的噪声，在神经网络中添加随机噪声可以带来正则化的效果。
4. batchnorm一般放在那里
   1. 一般放在线性层乘以权重参数后，放在激活函数前。
   2. BN是为了让输入进入激活函数的非饱和区，所以这样效果更好。
5. 为什么在做过正规化后，又要scale和shift呢
   1. 将分布拉扯到均值0，方差1附近，会丧失部分激活函数的非线性功能。比如sigmoid。所以添加scale和shift来偏移它们
   2. normalization相当于把上一层作出的努力磨平了，神经网络 可以自己琢磨前面的正规化W有没有起到优化作用，没有的话就"反"正规化，抵消之前的正规化操作带来的影响。
6. 给定一个张量[N, C, W]，batchnorm，和layernorm分别在哪层做归一化
   1. 画出图，认出哪个是一个样本，batchnorm就是对所有样本的一个维度做。layernorm对一个样本做
   2. batch norm: N, W
      1. $\gamma, \beta$大小为c
   3. layer norm：C, W
7. layernorm
   1. **LayerNormalization**是对一个样本进行处理，对一个样本的所有特征进行归一化，乍一看很没有道理，因为如果对身高体重和年龄一起求一个均值方差，
   2. 而此时我们对N个词进行Normalization等操作可以很好地反映句子的分布。
   3. nlp使用layernorm的理由
      1. bn不适用：1. 第一个位置是什么词都可以。2. 句子长度不一致
      2. layernorm的优点：可以很好的反映句子的分布。