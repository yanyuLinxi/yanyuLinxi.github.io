---
title: "Using RNN for Dexompiliation"
date: 2021-09-12T16:27:43+08:00
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
    - [预处理](#预处理)
- [5. 解决了什么问题（贡献）](#5-解决了什么问题贡献)
- [6. 实验结果](#6-实验结果)
- [7. 如何想到该方法](#7-如何想到该方法)
- [8. 我能否想到该方法](#8-我能否想到该方法)
- [9. 创新点是什么](#9-创新点是什么)
- [10. 如何用于本专业](#10-如何用于本专业)
- [11. 该方案还存在的问题](#11-该方案还存在的问题)
- [12. 注释](#12-注释)

# 1. 综述翻译

摘要——反编译，从二进制恢复源代码，
在许多需要分析或理解源代码不可用的软件的情况下很有用。源代码比二进制代码更易于人类阅读，并且有许多工具可用于分析源代码。现有的反编译技术通常会生成人类难以理解的源代码，因为生成的代码通常不使用程序员使用的编码习惯用法。与人工编写代码的差异也降低了分析工具对反编译源代码的有效性。解决反编译之间的差异问题
代码和人工编写的代码，我们提出了一种使用基于循环神经网络的模型反编译二进制代码片段的新技术。该模型学习源代码中出现的属性和模式，并使用它们生成反编译输出。我们在从 C 源代码编译的二进制机器代码片段上训练和评估我们的技术。我们在本文中概述的一般方法不是特定于语言的，并且几乎不需要或根本不需要语言及其属性或编译器如何运行的领域知识，从而使该方法可以轻松扩展到新的语言和结构。此外，该技术可以扩展并应用于传统反编译器不针对的情况，例如用于对孤立的二进制片段进行反编译；快速、按需反编译；特定领域的学习反编译；优化反编译的可读性；并恢复控制流结构、注释和变量或函数名称。我们表明这种技术产生的翻译通常是准确的或接近的，并且可以提供有用的图片

Disassembler(反汇编)(Machine Code to Assembly): A disassembler is a software tool which transforms machine code into a human readable mnemonic representation called assembly language.

Decompiler(反编译)(Binary Code to Source code): Software used to revert the process of compilation. Decompiler takes a binary program file as input and output the same program expressed in a structured higher-level language.


# 2. Tag

RNN; Decompiler; Binary Code; Translator; Abstract Syntax Tree(AST); AST

# 3. 任务描述

将二进制转为source code。

这个source code并不是truth source code，而是经过标记化的。就是将大多数字符串、变量、函数名进行替换，将其他的比如for this 等标识符标识为记号，然后进行还原。

# 4. 方法

backbone神经网络是Sequence-to-Sequence 模型 RNN。

数据集由C（source code）和与其一一匹配的二进制构成。

### 预处理
接下来的步骤对binary code 和 source code 进行相似的处理：
1. 将二进制和源代码进行序列化。
   1. 二进制采用byte-by-byte的方式组成token序列。（第二种方式：bite-by-bite，相比效果没前一种好）
   2. 源代码采用词法分析后转为token序列。
2. 源代码替换
   1. 将字符串替换为STRING
   2. 将top-20 函数名保留，其他函数名替换为function
   3. 将top-100 变量名保留，其他变量替换为var_XXX. XXX 是变量名的序号。
3. 标志化
   1. 将这些token转为one-hot向量。
4. 分桶
   1. 将二进制按照长度分成四个桶。这一步是因为RNN需要定长的输入和输出。所以需要针对长度不统一的序列进行padding或者舍弃。

将匹配好的匹配对，送入RNN进行训练。

# 5. 解决了什么问题（贡献）

# 6. 实验结果

实验结果的metrics：
> 我们比较预测的标记化输出 C 源代码由 RNN 针对标记化的已知基本事实值，采用两者之间的 Levenschtein 距离。

> 莱文斯坦距离，又称Levenshtein距离，是编辑距离的一种。指两个字串之间，由一个转成另一个所需的最少编辑操作次数。

edit distance大约在0.7左右。

# 7. 如何想到该方法

# 8. 我能否想到该方法

# 9. 创新点是什么

# 10. 如何用于本专业

# 11. 该方案还存在的问题

# 12. 注释
