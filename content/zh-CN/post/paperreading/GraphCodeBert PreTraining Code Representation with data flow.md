---
title: "GraphCodeBert PreTraining Code Representation With Data Flow"
date: 2022-04-06T11:19:46+08:00
tags : [
    "论文阅读笔记",
]
categories : [
    "论文阅读笔记",
]
series : []
aliases : []
draft: false
math: true
toc: true
---


## 1. 综述翻译

编程语言的预训练模型在代码搜索、代码完成、代码摘要等各种与代码相关的任务上取得了显着的经验改进。然而，现有的预训练模型将代码片段视为一系列标记，同时忽略了代码的固有结构，它提供了关键的代码语义并会增强代码理解过程。我们提出了 GraphCodeBERT，这是一种考虑代码固有结构的编程语言预训练模型。我们没有像抽象语法树（AST）那样采用代码的语法级结构，而是在预训练阶段使用数据流，这是一种代码的语义级结构，编码了“价值来自哪里”的关系”变量之间。这种语义级结构不太复杂，不会带来不必要的 AST 层次结构，其属性使模型更有效。我们基于 Transformer 开发 GraphCodeBERT。除了使用掩码语言建模任务外，我们还引入了两个结构感知预训练任务。一种是预测代码结构边缘，另一种是对齐源代码和代码结构之间的表示。我们使用图形引导的蒙面注意功能以有效的方式实现模型，以结合代码结构。我们在四个任务上评估我们的模型，包括代码搜索、克隆检测、代码翻译和代码细化。结果表明，代码结构和新引入的预训练任务可以提高 GraphCodeBERT 并在四个下游任务上实现最先进的性能。我们进一步表明，该模型在代码搜索任务中更喜欢结构级别的注意力而不是令牌级别的注意力。

### 1.1 发表于

ICLR 2021

## 2. Tag

bert; code semantic extraction; data flow; ast;

## 3. 任务描述

代码表征模型。在多个任务上进行训练。
1.code search
2.clone detection
3.code translation
4.code refinement

## 4. 方法

### 特点
从AST中提取data flow

1. data flow是一个图，图上的节点代表变量，边表示这些变量的值来自哪里。不像AST，data flow在相同的源代码的不同的抽象语法下是一样的。AST是提取了代码的syntactic-level结构信息，而data flow提取代码的semantic-level信息。同时，data flow有助于模型考虑离的很远距离但是使用了相同的变量或函数引起的长期依赖关系。例如下图的代码中有好几个地方都有x，通过提取到的data flow后，我们可以知道，x11会更加注意x7和x9而不是x3。
2. GraphCodeBert采用数据流而不是AST，是考虑到数据流图不像AST这么复杂，也不会带来不必要的深层信息。



### 输入：
给定源代码C={c1,c2,,Cn},对应的注释W={w1,w2,wm}.相应的数据流图G(C)=(V,E),V={v1,v2,}为变量序列，E={e1,e2,}为边集合，其中每条边代表数据流向。
输入包括以下部分：

+ 源代码C={c1,c2,...,Cn}
+ 对应的注释W={w1,w2,...,wm}
+ 变量序列V={v1,v2,...,vk}

最终输入的序列X为上面3个序列的连接
X={[CLS],W,[SEP] C,[SEP],V}

输入序列X会被转化为向量H^0。包括了token和position embedding。并对变量序列V使用了一种特殊的position embedding来标识它们是数据流图的一个结点。

### 模型：

在注意力机制中引入了M
$$head = s o ftmax ( \frac { Q _ { i } K^T_i}{\sqrt { d _ { k } } } + M ) V _ { i }$$

∣X∣表示输入序列的长度，包括 token序列, 注释序列，变量序列。M 是 Graph-Guided Masked Attention 矩阵

### Graph-Guided Masked Attention

这里用
+ v表示变量序列V第i个变量
+ c,表示源代码token集合C第i个token
+ E‘定义为，如果变量v与itoken/序列第j个token c;相关联，那么〈v,c〉/〈cj,v〉∈ E’

为了将图结构引入transformer,这里提出Graph-Guided Masked Attention来过滤不相关signal.graph--guided masked attention用矩阵M表示。

$M_{ij} = 0 <= if ( q _ { i } \in  [ C L S ] , [ S E P ] ) or  ( q _ { i } , k _ { j }\in W \cup C )  or ( < k _ { j } , k _ { j }> \in E \cup E' )$

$M_{ij} = -\infty <= otherwise$

负无穷在归一化的时候会归一化成0.所以用这种方式表示他们在dataflow中是有连接的。


### 预训练任务：
该模型以源代码和注释以及相应的数据流作为输入，并用标准的masked language模型应用在2个结构化预训练任务上：
1. data flow edges prediction数据流边预测，用来学习代码的结构化表示
   1. 摘掉边进行预测。引入了负采样。
2. variable-alignment across source code and data flow。源代码和数据流之间的变量分配，用于学习数据流结点来自源代码中哪个token。
   1. 该任务是为了学习数据流图与源代码之间的对应关系，与边预测不同的是，边预测学习的是变量序列 V VV 中2个结点之间的联系， 而变量分配任务学习的是源代码token序列 C和变量序列 V之间的联系， 也就是学习变量结点 v_i和token c_j对应的关系。


### 下游任务：
1. natural language code search，代码搜索
2. clone detection，克隆检测
3. code translation，代码翻译
4. code refinement，代码细化

## 5. 解决了什么问题（贡献）

## 6. 实验结果

## 7. 如何想到该方法

## 8. 我能否想到该方法

## 9. 创新点是什么

## 10. 如何用于本专业

## 11. 该方案还存在的问题

## 12. 注释
