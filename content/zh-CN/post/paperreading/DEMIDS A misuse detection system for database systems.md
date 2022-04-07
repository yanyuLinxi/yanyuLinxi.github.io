---
title: "DEMIDS a Misuse Detection System for Database Systems"
date: 2021-09-16T15:38:15+08:00
tags : [
    "论文阅读笔记",
    "异常行为分析",
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

尽管有必要保护存储在数据库系统 (DBS) 中的信息，但现有的安全模型不足以防止滥用，尤其是合法用户的内部滥用。此外，现有的误用检测研究尚未充分解决 DBS 中误用检测的概念。
重刑。即使有可用的方法来保护存储在数据库系统中的信息不被滥用。它们很少被保安人员使用
因为组织的安全策略要么不精确，要么根本不知道。 本文介绍了一种称为 DEMIDS 的误用检测系统，该系统专为关系数据库系统量身定制。 DEMIDS 使用审计日志来派生描述 DBS 用户典型行为的配置文件。计算出的配置文件可用于检测滥用行为，尤其是内部人员滥用。此外，配置文件可以通过帮助安全人员定义/优化组织，作为组织安全再造的宝贵工具
安全策略并验证现有的安全策略，如果提出的方法有任何必要，那么用户的访问模式
通常形成一些工作范围，其中包括通常与查询中的某些值一起引用的属性集。 DEMIDS 认为
通过距离度量的概念，在给定的数据库模式中编码的数据结构和语义的领域知识。距离度量用于指导搜索描述用户工作范围的频繁项集。在 DEMIDS 中，使用数据库管理系统的数据管理和查询处理功能从审计日志中有效地计算出此类频繁项集

# 2. Tag


# 3. 任务描述

(Carter and Katz 1996) revealed that in computer systems the primary security threat comes from insider abuse rather than from intrusion
然而，现实表明，这种强制执行组织安全策略的机制通常没有得到充分利用。 这有多种原因。 首先，安全策略通常不为人所知或没有很好地指定，因此很难甚至不可能将它们转换为适当的安全机制。 此观察结果适用于一般安全策略以及针对单个数据库用户和应用程序定制的策略。 其次，更重要的是，安全策略没有充分保护存储在数据库系统中的数据免受“特权用户”的侵害。 （Carter 和 Katz 1996）透露，在计算机系统中，主要的安全威胁来自内部人员滥用而不是入侵。 这一观察结果导致必须更加重视系统的内部控制机制，例如审计日志分析。


# 4. 方法

所提出的方法的本质是，给定数据库模式和关联的应用程序，用户的访问模式将形成一些工作范围，包括某些属性集，这些属性集通常与查询中的某些值一起引用。工作范围的概念在概念上被频繁项集的概念所捕获，频繁项集是具有某些值的特征集。基于数据字典中编码的数据结构和语义（完整性约束）以及审计日志中反映的用户行为，DEMIDS 定义了距离度量的概念，用于度量一组属性相对于工作范围的接近程度。通过利用数据库管理系统的高效数据处理功能的新型数据挖掘方法，距离度量用于指导在审计日志中搜索频繁项集。滥用，例如篡改数据的完整性，然后可以通过将派生的配置文件与指定的安全策略或收集的有关用户的新信息（审计数据）进行比较来检测。


不行，不是想要的。
# 5. 解决了什么问题（贡献）

# 6. 实验结果

# 7. 如何想到该方法

# 8. 我能否想到该方法

# 9. 创新点是什么

# 10. 如何用于本专业

# 11. 该方案还存在的问题

# 12. 注释