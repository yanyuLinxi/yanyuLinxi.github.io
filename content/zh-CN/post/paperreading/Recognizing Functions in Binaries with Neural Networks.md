---
title: "Recognizing Functions in Binaries With Neural Networks"
date: 2021-09-12T15:34:32+08:00
tags : [
    "论文阅读笔记",
]
categories : [
    "论文阅读笔记",
]
series : []
aliases : []
draft: false
---

# 目录： <!-- omit in toc -->
- [1. 综述翻译](#1-综述翻译)
- [2. Tag](#2-tag)
- [3. 任务描述](#3-任务描述)
- [4. 方法](#4-方法)
- [5. 解决了什么问题（贡献）](#5-解决了什么问题贡献)
- [6. 实验结果](#6-实验结果)
- [7. 如何想到该方法](#7-如何想到该方法)
- [8. 我能否想到该方法](#8-我能否想到该方法)
- [9. 创新点是什么](#9-创新点是什么)
- [10. 如何用于本专业](#10-如何用于本专业)
- [11. 该方案还存在的问题](#11-该方案还存在的问题)
- [12. 注释](#12-注释)

# 1. 综述翻译

二进制分析有助于许多重要的应用程序，如恶意软件检测和自动修复易受攻击的软件。在本文中，我们建议应用人工神经网络来解决二元分析中重要而困难的问题。具体来说，我们解决了函数识别问题，这是许多二进制分析技术中至关重要的第一步。尽管神经网络在过去几年经历了复兴，在视觉对象识别、语言建模和语音识别等多个应用领域取得了突破性的成果，但还没有研究人员尝试将这些技术应用于二进制问题。分析。使用来自先前工作的数据集，我们表明循环神经网络可以比最先进的基于机器学习的方法更准确和更高效地识别二进制文件中的函数。我们可以更快地训练模型一个数量级，并以数百倍的速度对二进制文件进行评估。此外，它在八个基准测试中的六个基准上将错误率减半，并且在其余两个基准上的表现相当。

# 2. Tag

Binary Code Analysis, RNN, NLP, Function Recognizing. 

# 3. 任务描述

Function start identification: Given C, find { f1,1, ·· · , fn,1}. In other words, recover the location of the first byte of each function.

* Function end identification: Given C, find { f1,l1, ·· · , fn,ln}. In other words, find the bytes
where each of the n functions in the binary ends. The length of each function is not given.
* Function boundary identification: Given C, find {( f1,1, f1,l1) ·· · , ( fn,1, fn,ln )}. In other words, dis-cover the location of the first and last byte within each function This task is more than a simple com- bination of function start and end identification. If the starts and ends of functions have been identi- fied separately, they need to be paired correctly so that each pair contains the start and end of the same function.
* General function identification: Given C, find {( f1,1, f1,2, ·· · , f1,l1) ·· · , ( fn,1, fn,2, ·· · fn,ln )}; i.e.,determine the number of functions in the file, and all of the bytes which make up each function.

# 4. 方法

创建标签：

> 我们将代码 C 本身视为一个字节序列 C[0],C[1],···,C[l]，其中C[i]∈$Z_{256}$是序列中的第i个字节。 我们将二进制中的 n 个函数表示为 f1,····,fn。 我们将属于每个函数 fi 的代码字节的索引（即对应于在运行该函数时可能执行的指令的字节）标记为 fi,1,···,fi,li，其中 li 是fi 中的总字节数。 不失一般性，我们假设 fi,1 < fi,2 < ·· · < fi,k。 每个字节可能属于任意数量的函数，函数可以包含任何字节集，无论是否连续。

为什么使用字节而不是指令：

> 请注意，我们将代码和函数定义为字节集合而不是指令集合。 在 x86 和 x86-64 ISA 中，根据解码开始的偏移量，字节序列可以有许多合理的指令解码； 因此每个字节可能属于少数可能的指令。 以字节为单位工作使我们能够避免这种歧义。

将二进制按byte字节一个个送入双向LSTM判断，其是否是函数的开头和结尾。

![双向LSTM](/researchPng/research/BiLSTM.png)

注意：论文分别训练了两个网络判断是否是函数开头或者结尾。

# 5. 解决了什么问题（贡献）

论文中的一个示例很有意思：

![binaryCodeExample](/researchPng/research/binary_code_example.png)

原文：

在图 1 中，我们展示了一个简短的 C 函数示例以及在两个不同优化级别编译后的相应二进制代码。

图 1b 中的代码包含非常清晰的函数开始和结束标记：push %rbp 和 mov %rsp,%rbp 的函数序言保存了调用者的堆栈帧，函数以 retq 结束，它在函数中的其他任何地方都没有出现。相比之下，图 1c 根本不使用堆栈，因此函数开始时对 edi 和 esi 中传递的函数参数进行了一些访问；寻找 push %rbp 会失败。此外，对参数的类似访问再次出现在函数体内，因此很难仅仅依靠它作为函数开始的标记。同样，retq 在代码中出现两次，因此当我们看到这条指令时预测函数结束将失败。

这个例子说明了为什么函数识别会带来很多困难，简单的启发式方法不太可能足够，这与直觉可能建议的相反。



# 6. 实验结果

> 按照 Bao 等人的程序进行操作。 我们为四种（架构、操作系统）配置中的每一种都训练了一个单独的模型。 为了报告可比较的结果，我们还使用了 Bao 等人的 10 倍交叉验证； 我们为四种配置中的每一种训练十个模型，其中十个模型中的每一个都使用不同的 10% 的二进制文件作为测试集。

实验效果看论文呢，基本非常好。准确率普遍95%以上

论文提出了两个limitations：

1. 在测试集没有出现的binaries上效果可能会较差
2. 抗混淆性可能不够。如在一段话中插入连续无意义的NOP，不会影响函数功能，但是会影响神经网络的判断。

# 7. 如何想到该方法

# 8. 我能否想到该方法

# 9. 创新点是什么

# 10. 如何用于本专业

# 11. 该方案还存在的问题

论文中说的future work：

> 尽管我们已经看到了一些关于 RNN 在各种条件下的性能的实验证据，但我们缺乏对模型内部机制的清晰解释。一种可能的解释方法是通过特征向量结构的分析来进行，方法是在网络随时间演变时线性化网络状态，并分析线性化系统的哪些特征向量携带与任务相关的信息 [12]。这种分析可以了解网络在选择、集成和通信相关信息时如何忽略不相关信息，并允许识别线性化系统的哪些特征向量负责网络执行的这些任务。然而，如果对破坏模型准确性感兴趣的对手可以使用神经网络的参数，他们可能能够使用这种分析来更有效地添加额外的指令，这些指令与携带任务相关信息的特征向量不正交，从而阻止其传输并显着影响 RNN 的性能。


# 12. 注释
