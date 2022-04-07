---
title: "Gensim学习笔记"
date: 2021-10-22T10:29:55+08:00
tags : [
   "python相关库学习"
]
categories : [
   "学习"
]
series : []
aliases : []
draft: false
---

# 使用腾讯中文语料库

> 腾讯词向量使用方法： https://www.jianshu.com/p/65a29663130a  

> 语料库地址： https://ai.tencent.com/ailab/nlp/zh/embedding.html

# 语料库
1. chinese-word-vectors:
   1. https://github.com/Embedding/Chinese-Word-Vectors
   2. 300维
2. 腾讯词向量：
   1. https://www.jianshu.com/p/65a29663130a 
   2. 200维，800万词。
3. 其他多语言语料库
   1. https://sites.google.com/site/rmyeid/projects/polyglot

# 使用gensim 来读取预训练语料库

