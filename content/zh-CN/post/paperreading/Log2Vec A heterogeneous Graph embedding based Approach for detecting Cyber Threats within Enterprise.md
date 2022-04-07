---
title: "Log2Vec a Heterogeneous Graph Embedding Based Approach for Detecting Cyber Threats Within Enterprise"
date: 2021-09-25T14:45:30+08:00
tags : [
    "论文阅读笔记",
    "异常行为分析",
    "Insider Threat",
    "GNN",
    "Doc2Vec",
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
  - [概览](#概览)
  - [Graph Construction](#graph-construction)
  - [关系详细定义](#关系详细定义)
  - [Graph Embedding](#graph-embedding)
  - [Detection](#detection)
    - [k-means簇聚类算法简单讲解：](#k-means簇聚类算法简单讲解)
    - [log2Vec 的聚类算法](#log2vec-的聚类算法)
  - [random walk](#random-walk)
- [5. 解决了什么问题（贡献）](#5-解决了什么问题贡献)
- [6. 实验结果](#6-实验结果)
- [7. 如何想到该方法](#7-如何想到该方法)
- [8. 我能否想到该方法](#8-我能否想到该方法)
- [9. 创新点是什么](#9-创新点是什么)
- [10. 如何用于本专业](#10-如何用于本专业)
- [11. 该方案还存在的问题](#11-该方案还存在的问题)
- [12. 注释](#12-注释)

# 1. 综述翻译

内部员工的常规攻击和新兴的 APT 都是组织信息系统的主要威胁。现有的检测主要集中在用户的行为上，通常分析记录他们在信息系统中操作的日志。一般来说，这些方法中的大多数都考虑了日志条目之间的顺序关系并模拟用户的顺序行为。然而，他们忽略了其他关系，不可避免地导致在各种攻击场景下的表现不尽如人意。我们提出 log2vec，一种基于异构图嵌入的模块化方法。首先，它涉及一种启发式方法，该方法根据日志条目之间的不同关系将日志条目转换为异构图。接下来，它利用适用于上述异构图的改进图嵌入，可以自动将每个日志条目表示为低维向量。 log2vec 的第三个组件是一种实用的检测算法，能够将恶意和良性日志条目分成不同的集群并识别恶意条目。我们实现了 log2vec 的原型。我们的评估表明 log2vec 明显优于最先进的方法，例如深度学习和隐马尔可夫模型 (HMM)。此外，log2vec 显示了其在各种攻击场景中检测恶意事件的能力。


## 1.1 发表于

2019 于 Computer and Communications Security (CCS) A会

# 2. Tag

Cyber Threat; Enterprise; Anomaly detection; GNN; Doc2Vec

# 3. 任务描述

现代信息系统已成为当今企业和组织的重要且不可替代的组件。然而，这些系统经常面临来自内部员工的攻击风险，他们授权访问它们并故意使用这种访​​问来影响它们的机密性、完整性或可用性。同时，另一种新兴攻击，高级持续威胁 (advanced persistent threat APT) 也威胁着这些系统。具体来说，APTactors 最初会破坏目标系统中的帐户和主机，然后从这些主机中，他们会通过内网秘密地、持续地破坏多台主机并窃取机密信息

常见攻击模式:
对抗模型包括以下三种企业和政府常见的攻击场景。 第一种情况是内部员工滥用职权进行恶意操作，例如访问数据库或应用服务器，然后破坏系统或窃取知识产权以谋取个人利益。 二、恶意内部人员获取其他合法用户的凭据
用户通过窥视或键盘记录器，并利用这个新身份来寻求机密信息或在公司中制造混乱,利用这个新身份窃取机密信息（即伪装攻击） 。这两种场景属于典型的内部员工攻击。 第三种攻击是 APTactor 破坏系统中的一台主机，并从该主机上持续破坏多台主机以提升其权限并窃取机密文件。

现有的方法通常将用户的各种操作（也包括日志条目）转换为可以保存信息的序列，例如日志条目之间的顺序关系，然后使用顺序处理技术，例如。深度学习，从过去的事件中学习并预测下一个事件 [12, 47]。本质上，这些日志条目级方法对用户的正常行为进行建模，并将与其的偏差标记为异常。

总之，我们面临三个问题：1）如何同时检测上述两种攻击场景，特别是考虑到检测系统的所有三种关系（sequential relationship among log entries, logical relationships among days, interactive relationship among hosts,）； 2）如何在APTscenario中进行细粒度的检测，特别是深度挖掘和分析主机内日志条目之间的关系； 3）如何在没有攻击样本的情况下对训练模型进行检测。



# 4. 方法

## 概览
Log2vec 包含三个组件，如图 1 所示： (1) Graph构建。 Log2vec 构建异构图来整合日志条目之间的多种关系； (2) 图嵌入（也是图表示学习）。这是一种强大的图处理方法，可以根据每个操作在此类图中的关系来学习它们的表示（向量）。对用户的操作进行矢量化，可以直接比较他们的相似性以找出异常； (3) 检测算法，有效地将恶意操作分成单独的集群和弄清楚他们。

![figure1](/researchPng/research/insiderthreatgnn.png)


+ 首先，log2vec 的第一个组件构建了一个异构图。这个数据结构是基于前面的三个关系构建的，这是现有方法在解决两种攻击场景中使用的主要关系[4,12,38,41,47,50,57]（对于问题1） .
+ 其次，我们将日志条目划分为五个属性。根据这些属性，我们深入考虑主机内日志之间的关系，并设计出精细的规则来关联它们。这种设计使正常和异常的日志条目在这样的图中拥有不同的拓扑结构，可以被 log2vec 的后面组件捕获和检测（对于问题 2）。
+ 第三，log2vec 的图嵌入和检测算法在没有攻击样本的情况下将日志条目表示并分组到不同的集群中，适用于数据不平衡的场景（对于问题 3）。此外，图嵌入本身可以为每个操作自动学习表示（向量），而不是手动提取特定领域的特征，从而独立于专家的知识。我们的改进版本可以进一步从上述异构图中差分提取和表示操作之间的多种关系。

## Graph Construction
Log2vec 的第一个组件是一种基于规则的启发式方法，用于将反映用户典型行为和暴露恶意操作的日志条目之间的关系映射到图形中。log2vec主要考虑了三种关系：（1）causal and sequential relationships within a day 一天内的因果关系和顺序关系； (2) logical relationships among days 多天内的逻辑关系
(3) logical relationships among objects.对象之间的逻辑关系。

1. 我们将日志条目分为五个主要属性（主题、对象、操作类型、时间和主机），称为元属性（参见第 3.1 节）这就将构建了一个异构图的基本元素。
2. 在设计关于这三种关系的规则时，我们会考虑这些元属性的不同组合，以关联更少的日志条目并将更精细的日志关系映射到图中。我们使用一个规则，将同一用户的日志条目按时间顺序连接起来（规则 A），将这种关系映射到图形中。 我们考虑两个元属性，主题和时间
3. 在另一个例子中，我们考虑另一个元属性，操作类型，并使用一个规则，将同一用户和同一操作类型的日志条目按时间顺序连接起来（规则B），将一天内的设备连接操作串联起来。在生成对应于 3 天的三个设备连接序列后，我们使用其他规则根据它们的相似性将它们关联起来。
4. 通过日志属性的不同组合，我们设计了涉及较少日志条目的各种行为序列，并将一天内和主机内的日志条目之间的多个更精细的关系映射到图中。 经过图嵌入和检测算法，log2vec 产生小簇来揭示异常操作。 在实践中，可疑集群中涉及的日志条目数量非常少，甚至等于1。因此，log2vec在上述两种攻击场景中对用户的行为进行了更精细的挖掘。
5. 根据 log2vec 中的每条规则，我们将日志条目转换为序列或子图，所有这些都构成了一个异构图。 每个规则，对应一个边类型，是从一个特定的关系派生出来的，如上例。 由于不同的关系在各种场景中扮演不同的角色，我们使用多种边类型而不是权重来区分它们。

## 关系详细定义

A log entry： < sub, obj,A,T,H >
其中sub是用户的集合。obj 是对象的集合，例如文件、移动存储设备和网站； A是操作类型的集合，如文件操作、浏览器使用等； T 是时间的集合，H 是主机的集合，例如计算机或服务器。

此外，sub、obj、A 和 H 都有自己的属性集。sub 的属性涉及角色（例如系统管理员）和他所属的组织单位（例如现场服务部门）。 obj 的属性可能包括文件类型和大小。 H 的属性是服务器的功能（例如文件服务器）。也就是说，它把一个登录操作当作如下方式，一个用户（子）登录到（A）一个目的主机（obj） 源一 (H)，就像用户在服务器中写入文件一样。

关系涉及三类：（1）一天内的因果关系和顺序关系； (2) 天之间的逻辑关系； (3)对象之间的逻辑关系。



> Rule1 (edge1): log entries ofthe samedayare connectedin chronological order with the highest weight (value 1).
> 
> Rule1（edge1）：按时间顺序连接当天的日志条目，权重最高（值为1）。

> Rule2 (edge2): log entries ofthe same host and the same day are connected in chronological order with the highest weight (value 1).
> 
> 规则2（edge2）：同一主机同一天的日志条目按时间顺序连接，权重最高（值为1）。


> Rule3 (edge3): log entries ofthe same operation type, the same host and the same day are connected in chronological order with the highest weight (value 1)
> 
> 规则 3（边 3）：相同操作类型、相同主机和同一天的日志条目按时间顺序连接，权重最高（值 1）


不同于恶意的行为模式。为了比较从 rule1∼rule3 导出的用户日常行为序列，我们提出 rule4∼rule6，包括分别对应于 rule1∼rule3 的元属性的元属性。通过这些规则，log2vec 分别隔离了异常的行为序列，
来自图中第 3.2.1 节中提到的各种场景。

> Rule4 (edge4): daily log sequences are connected and their weights are positively related to similarity ofthe numbers oflog entries that they contain.
> 
> Rule4（edge4）：每日日志序列是连通的，它们的权重与它们包含的日志条目数量的相似性呈正相关。

> Rule5 (edge5): daily log sequences ofthe same host are connected and weights are positively related to similarity ofthe numbers oflog entries that they contain.
> 
> Rule5（edge5）：同一主机的每日日志序列是相连的，权重与它们包含的日志条目数量的相似性呈正相关。

> Rule6 (edge6): daily log sequences of the same operation type and the same host are connected and weights are positively related to similarity ofthe numbers of log entries that they contain.
> 
> Rule6（edge6）：相同操作类型和相同主机的每日日志序列是相连的，权重与它们包含的日志条目数量的相似度呈正相关。

> Rule7 (edge7): log entries of accessing the same destination host from the same source host with the same authentication protocol are connected in chronological order with the highest weight (value 1). 
> 
> Rule7（edge7）：使用相同认证协议从同一源主机访问同一目标主机的日志条目按时间顺序连接，权重最高（值为1）。

> Rule8a (edge8): log sequences of the same destination host and source one with different authentication protocols are connected and weights are positively related to the similarities of the numbers of log entries that they contain. 
> 
> Rule8a (edge8)：同一目标主机的日志序列和具有不同身份验证协议的源 1 连接在一起，权重与它们包含的日志条目数量的相似性呈正相关。

> Rule8b (edge8): log sequences of different destination hosts or source ones with the same authentication protocol are connected and weights are positively related to the similarities of the numbers of log entries that they contain.
> 
> Rule8b（edge8）：具有相同认证协议的不同目的主机或源主机的日志序列相连，权重与它们包含的日志条目数量的相似性呈正相关。


> ule9 (edge9): log entries of the same host and accessing the same domain name are connected in chronological order with the highest weight (value 1).
> 
> Rule9（edge9）：同一主机访问同一域名的日志条目按时间顺序连接，权重最高（值为1）。

> Rule10 (edge10): log sequences of the same host and different domain names are connected and weights are positively related to the similarities of accessing modes and numbers of log entries that they contain.
> 
> Rule10（edge10）：同一主机不同域名的日志序列是相连的，权重与访问方式的相似性和它们所包含的日志条目数呈正相关。

对于每个类别，我们根据元属性的不同组合提出了一些规则。 如图3所示，我们首先提出rule1∼rule3将一天内的日志条目连接成序列，对应关系（1）。 这三个规则从不同方面对用户的行为进行建模，例如 日期、主机和操作类型。 通过这种设计，将用户在陌生主机上进行的操作，或者属于很少进行操作的操作类型，在图中进行隔离。 然后，我们提出了规则 4∼规则 6，以根据关系 (2) 分别桥接这些日常序列。 异常行为序列将与良性行为序列分开。 这六个规则将图 2c 中的关系映射到图形中。 它们主要关联用户跨天在多个主机上的各种类型的操作。

最后，提出了与关系（3）相对应的四个规则（rule7∼rule10），以考虑用户如何登录/入侵主机并向外部发送机密数据。 具体来说，它们构建了用户登录和网页浏览操作的模式。 有关登录操作的规则，规则 7 和规则 8，考虑如何在内联网内交互访问这些主机，例如图 2d 中的实例。 Web 操作规则，规则 9 和规则 10，侧重于用户通过 Internet 使用浏览器。 Intranet 和 Internet 是主要的入侵源，例如 登录主机或驱动下载。

## Graph Embedding
具体来说，图嵌入涉及图 1 中的随机游走和 word2vec。

假设一个walker 位于图中的一个节点上，他根据每条边的权重和类型决定下一个要访问的节点。 由他生成的路径，一个节点序列，被视为这些节点的上下文（见第 4.1 节）。 例如，当一个步行者驻留在属于第1天或第2天设备连接序列的节点时（图2a），通过图构建生成，他很少会选择第3天序列中的节点（设备连接），因为链接低 重量。 同样，当他在第 3 天的序列中驻留节点时，他很少会到达第 1 天或第 2 天的序列。

## Detection 
Log2vec 采用聚类算法对上述向量进行分析，并将良性操作（日志条目）和恶意操作分为不同的集群（第 5.1 节）。

在聚类之后，我们设置了一个阈值来识别恶意集群。 也就是说，大小小于阈值的集群被视为恶意（第 5.2 节）

### k-means簇聚类算法简单讲解：
1. 定义总共有多少个簇
2. 将每个簇心随机定在一个点上
3. 将每个数据节点关联到最近簇重心所属的簇上
4. 对于每一个簇找到其所有关联点的中心点（取每一个点坐标的平均值）
5. 将上述点变为新的簇心
6. 不停重复直至每个簇所拥有的点不变。

简单来说，聚类算法只是通过某种方式，将结果进行分类。

### log2Vec 的聚类算法
传统的更新聚类中心的想法，如k-means，不适合内部威胁检测，因为它严重依赖于聚类中心和k的初始化，导致性能不理想。这里提出了一个新的聚类算法，见论文。



## random walk
Log2vec 的改进是控制邻居节点 (neigh) 的数量并以不同比例的边类型 (ps) 集提取上下文，旨在解决不平衡数据集和各种攻击场景的问题。

改进版的random walk

# 5. 解决了什么问题（贡献）

1. 提出了一种将log日志转为图结构的方法
2. 设计了很多规则，使用这些规则，提出了异构图来构造图。异构图可以允许更多类型的节点互相交互，比如日志文件，用户，操作等。从实验结果来看，异构图会比同构图要好一点。

问题：

1. 整个方案非常复杂，复现可行度需要画一个问号。

# 6. 实验结果

详见Table 3 和 Table 4.

# 7. 如何想到该方法

# 8. 我能否想到该方法

# 9. 创新点是什么

# 10. 如何用于本专业

# 11. 该方案还存在的问题

# 12. 注释
