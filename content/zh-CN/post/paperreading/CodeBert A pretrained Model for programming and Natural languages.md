---
title: "CodeBert a Pretrained Model for Programming and Natural Languages"
date: 2022-04-06T10:48:22+08:00
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

我们展示了 CodeBERT，一种用于编程语言 (PL) 和自然语言 (NL) 的双峰预训练模型。 CodeBERT 学习支持下游 NL-PL 应用程序的通用表示，例如自然语言代码搜索、代码文档生成等。我们使用基于 Transformer 的神经架构开发 CodeBERT，并使用包含预训练的混合目标函数对其进行训练替换令牌检测的任务，即检测从生成器中采样的似是而非的替代方案。这使我们能够利用 NL-PL 对的“双峰”数据和“单峰”数据，前者为模型训练提供输入标记，而后者有助于学习更好的生成器。我们通过微调模型参数在两个 NL-PL 应用程序上评估 CodeBERT。结果表明，CodeBERT 在自然语言代码搜索和代码文档生成方面都取得了最先进的性能。此外，为了研究在 CodeBERT 中学习了什么类型的知识，我们构建了一个用于 NL-PL 探测的数据集，并在预训练模型的参数固定的零样本设置中进行评估。结果表明，CodeBERT 在 NL- 上的表现优于以前的预训练模型PL 探测.1

### 1.1 发表于

EMNLP 2020

## 2. Tag

代码语义; Bert; Code Semantic; CodeBert; Natural Language; Multi-tasks;

## 3. 任务描述

特征提取模型，用于提取语义特征，并不针对某个任务。

CodeBERT是一种可处理双模态数据（编程语言PL和自然语言NL）的预训练模型，支持下游 NL-PL 应用程序(如自然语言代码搜索、代码文档生成等)的通用表示。

CodeBERT基于 Bert 的架构开发，混合目标函数结合了替换标记检测的预训练任务。

在两个 NL-PL 下游任务上微调，结果显示在自然语言代码搜索和代码文档生成任务上达到了SOTA。此外，文章还构建了一个用于 NL-PL 探测的数据集，并在预训练模型的参数固定的零样本设置中进行了评估。


## 4. 方法

输入： [CLS], w1, w2, …wn,[SEP],c1, c2, …, cm,[EOS]
w为NL单词序列，c为PL token序列。[CLS]为两个片段前的特殊token。
输出：自然语言和代码中每个token的上下文向量表示，以及[CLS]的表示，作为聚合序列的表示

### 预训练任务：

数据：
1. 双峰NL-PL 对是指类似下面的自然语言-程序语言对，即带有配对文档的单独函数，语料一般以json行格式文件保存，一行是一个json对象：

```json
{
  "nl": "Increment this vector in this place. con_elem_sep double[] vecElement con_elem_sep double[] weights con_func_sep void add(double)",
  "code": "public void inc ( ) { this . add ( 1 ) ; }"
}
```
2. 单峰数据是指没有成对自然语言文本的单独函数代码和没有成对代码的自然语言

任务：
1. MLM任务 (Masked Language Modeling)
   1. 对NL-PL双峰数据对应用MLM，即选择随机位置的NL和PL mask，用特殊token [MASK]代替
   2. MLM的目标是预测被mask的token。鉴别器$p^{D_i}$预测第i个单词为masked的token的概率
   3. $L _ { M L M }( \theta ) = \sum _ { i \in m^w \cup  m^c } - \log p ^ { D _ { 1 } } ( x _ { i } | w ^ { m a s k e d } , { c ^ { m a s k e d } } )$
   4. 公式意思就是针对被mask的值，$p^D$从一个大的字典库中预测出他们。
2. RTD任务（Replaced Token Detection)
   1. 使用双峰数据。训练时同时使用双峰数据和单峰数据，有两个数据生成器$p^{G_w}, p^{G_c}$，一个生成NL，一个生成PL，用于选择随机掩蔽位置。生成器随机找一个位置使用生成的token进行代替。
   2. 鉴别器$p^{D_2}$鉴别是否正好生成了原始单词，即第i个单词为原始单词的概率。
   3. $L _ { R T D } ( \theta ) = \sum _ { i = 1 } ^ { | w | + | c | } ( \delta ( i ) \log p ^ { D_2 } ( x ^ { \operatorname { corrupt} } , i ) + ( 1 - \delta ( i ) ) ( 1 - \log p ^ { D_2 } ( x ^ { \operatorname { corrupt}} , i ))$
   4. 就是针对每个单词判断它为原始词的概率。
3. 两个任务的组合：
   1. $$m i n L_{MLM} ( \theta ) + L _ { R T D } ( \theta )$$

#### 数据处理
1. 1)每个项目应该被至少一个其他项目使用，(2)每个文档被截断到第一段（图中红色表示），(3)小于三个标记的文档被删除，(4)小于三行的函数被删除，(5)带有子字符串“test”的函数名被删除。图13给出了一个数据示例。


### 实验任务

1. 自然语言代码搜索
   1. 微调
   2. 不用微调
2. 代码文档生成
   1. 微调
   2. 不用微调



## 5. 解决了什么问题（贡献）

## 6. 实验结果

## 7. 如何想到该方法

## 8. 我能否想到该方法

## 9. 创新点是什么

## 10. 如何用于本专业

## 11. 该方案还存在的问题

## 12. 注释
