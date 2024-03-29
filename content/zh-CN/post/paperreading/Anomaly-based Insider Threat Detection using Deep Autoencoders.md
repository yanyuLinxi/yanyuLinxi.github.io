---
title: "Anomaly Based Insider Threat Detection Using Deep Autoencoders"
date: 2021-09-16T20:21:40+08:00
tags : [
    "论文阅读笔记",
    "异常行为分析",
    "Unsupervised",
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
  - [1.1 发表](#11-发表)
- [2. Tag](#2-tag)
- [3. 任务描述](#3-任务描述)
- [4. 方法](#4-方法)
  - [概览](#概览)
  - [特征提取：](#特征提取)
  - [自编码器](#自编码器)
- [5. 解决了什么问题（贡献）](#5-解决了什么问题贡献)
- [6. 实验结果](#6-实验结果)
- [7. 如何想到该方法](#7-如何想到该方法)
- [8. 我能否想到该方法](#8-我能否想到该方法)
- [9. 创新点是什么](#9-创新点是什么)
- [10. 如何用于本专业](#10-如何用于本专业)
- [11. 该方案还存在的问题](#11-该方案还存在的问题)
- [12. 注释](#12-注释)

# 1. 综述翻译

近年来，恶意内部人员威胁已成为组织可能面临的最重要的网络安全威胁之一。由于内部人员具有逃避部署的信息安全机制（例如防火墙和端点保护）的天然能力，因此检测内部人员威胁可能具有挑战性。此外，与组织为入侵/异常检测目的收集的审计数据量相比，恶意内部人员的行为留下的数字足迹可能微不足道。为了从大量复杂的审计数据中检测内部威胁，在本文中，我们提出了一种检测系统，该系统使用深度自动编码器的集合来实现异常检测。集成中的每个自动编码器都使用特定类别的审计数据进行训练，这些数据准确地代表了用户的正常行为。原始数据和解码数据之间获得的重建误差用于衡量任何行为是否异常。在数据经过单独训练的自动编码器处理并获得各自的重建误差后，使用联合决策机制报告用户的整体恶意评分。使用用于内部威胁检测的基准数据集进行数值实验。结果表明，所提出的检测系统能够以合理的误报率检测所有恶意的内部人员行为。

## 1.1 发表

2018-ICDMW，数据库B会的workshop

# 2. Tag

Insider threat; Autoencoders; Unsupervised


# 3. 任务描述

# 4. 方法

## 概览

在我们提议的内部人员检测系统中，我们总共创建了四个检测器，分别用于四类审计数据，即登录/注销活动记录、文件操作、USB 设备操作和 http 活动记录。假设用户的行为在整个审计数据集中是一致的，则为审计数据的每个类别提取许多基于频率的特征。这些特征用作训练深度自动编码器的输入。

当经过训练的自动编码器充当特定正常用户行为的基线模型时，任何受恶意行为影响的特征向量都应显着偏离基线模型，并应报告为异常。

由于自动编码器由编码器和解码器组成，因此偏差是通过使用解码器重建编码特征向量时产生的误差来衡量的。在四个自编码器检测器运行完数据后，对每个检测器应用 top-N 推荐算法，产生四维归一化的顶部异常向量。

然后，我们将异常向量归因于用户，并对每个用户的异常向量进行加权以获得恶意评分。随后再次应用top-N推荐算法以报告具有最高恶意评分的用户以供进一步调查。

我们使用 CMU 的内部威胁测试数据集进行数值实验，以评估每个自动编码器的最佳构造，这些参数包括层数、激活函数类型和损失函数类型等各种参数。最后，我们证明了我们可以构建一个检测系统，该系统结合了不同的自动编码器架构，以可管理的误报率检测恶意内部攻击。特别是，本文做出了以下贡献：

具体：
1. 我们使用了基于主机的数据（即登录/注销活动、文件操作和 USB 设备操作）和基于网络的数据（即 http 活动）。
2. 为每个类别的数据集提取了许多特征。这些特征被转发到自动编码器，从而形成一个对用户行为进行建模的神经网络。换句话说，每个自编码器代表给定审计数据集的特定基线模型，任何偏离模型的行为（即可检测的自编码器重建错误）都应标记为“异常”。
3. 当所有自动编码器模型组合在一起时，可以从各种不同的审计数据视图中更好地识别用户的行为。一般而言，每个审计数据集可能仅提供微弱或不提供异常行为的指示。然而，当模型被用作异常行为的弱指标集合时，用户的恶意行为水平可能会被检测到。

概览总结：提取四种数据的特征=》自编码器重构，产生误差=》训练=》topN计算前N个恶意行为=》对每个用户使用topN计算恶意行为。

## 特征提取：

1. 时间粒度通常是一个需要考虑的关键因素，它可以确保提取的特征能够反映用户的正常行为，同时能够检测任何异常/异常变化。一方面，小粒度通常会引入大方差，从而产生过拟合的基线模型。另一方面，大的时间粒度将导致无法突出任何异常行为的欠拟合基线模型。在我们提出的系统中，我们将时间粒度设置为每小时，因为就文献中观察到的内容以及我们在实验中获得的内容而言，这是最合适的程度。所有特征均从用户每天（24 小时）的活动中提取
2. 计算每个用户的每小时登录频率以描述用户的每日登录行为/模式。 直观地说，这种登录模式对于用户来说很常见，因为他们通常在固定时间开始一天，比如 8:00 AM 或 9:00 AM。 同样，每个登录事件都会有一个相应的注销事件。 生成的每小时登录/注销模式形成一个长度等于 48 的正整数向量
3. 文件审计数据提供有关用户对文件的操作的信息； 例如，对此类文件进行的操作（例如，打开、写入、复制和删除）以及文件传输到的位置。 这里应用与登录/注销相同的概念，以提取文件操作特征，即获取每个用户的每种类型文件操作的每小时频率。 对于来自同一业务单元的一组用户，期望用户以类似的方式访问和操作文件，这体现在文件副本数量等特征上。 否则，如果用户执行文件复制的频率明显高于基线建议的频率（根据他/她自己的个人资料和他/她在组织中的同事的个人资料），则应引发关注事件。 随后将所有四种文件操作模式串联起来，生成由 96 个正整数组成的文件审计特征向量。
4. USB 设备审计数据记录用户是否已将拇指驱动器连接到/从其计算机主机断开连接，并记录访问了哪些目录。 将文件从用户计算机传输到拇指驱动器通常与恶意内部人员行为密切相关。 事实上，它已被确定为从计算机网络中窃取数据的三种最常见方法之一 [3]。 在所提出的系统中，我们将拇指驱动器连接和断开操作的每小时频率统计数据连接在一起，产生 48 个正整数的特征向量。
5. 传统上，http 审计数据能够提供非常丰富的信息，包括用户如何访问 Internet、数据如何传入和传出网络，甚至计算机与网络的交互行为模式。 然而，我们的工作旨在以有效和高效的方式检测恶意内部人员，因此，我们只关注用户在操作层面的活动。 特别是，用户基于 http 的活动被限制为三种类型，即：访问、上传和下载。 访问活动表示用户正在浏览网页； 一旦用户通过 HTTP 协议传出数据，这个活动就会触发一个上传活动； 相反，通过 HTTP 协议接收数据会触发下载活动。 http 审计数据特征向量连接每个活动的每小时频率。 这会产生 72 个正整数的特征向量。
6. 表一总结了审计数据的提取特征。 从每一类审计数据中提取的特征然后被转发到一个单独的自动编码器。 自编码器从每个特征向量中提取最常见的信息模式。 然后，通过研究自动编码器重建特征向量的程度，我们可以确定用户的日常行为是否与以前的行为不同，以及它与他/她的同龄人的行为有何不同。
![图1](/researchPng/research/autoencoders.png)

总结：特征提取部分每一天都提取了24个小时的特征，每个日志文件每小时提取2-4个特征，总共就提取了48-96个特征。训练时使用前k个做训练，使用第k+1天做测试。

## 自编码器
从异常检测的角度，我们希望将用户的正常行为表征为等同于该用户或用户组的基线模型。任何恶意行为都可能被识别为与基线模型的偏差。

在对用户的正常行为建模时，我们面临两个挑战：1）审计数据中存在复杂的非线性关系（例如，用户登录计算机的时间不一定与用户实际在计算机上花费的时间相关），以及2）很少有标签（如果有的话）可以提前表明“好”和“坏”审计数据实例，这意味着我们被迫进行无监督或半监督

我们使用深度自动编码器，因为它能够表示非线性关系，更重要的是，作为神经网络家族的一员，它用于无监督学习。

自编码器的有效性在很大程度上取决于自编码器模型及其相关参数的正确构建。例如，需要考虑各种参数，例如要采用的损失函数、要选择的层数以及对于每一层要采用的最佳激活函数。这些参数可能会对性能产生显着影响。在这项研究中，我们优化了这些自动编码器参数，

自编码器：
编码：$z=f(Wx+b)$

解码: $x'=f'(W'z+b')$

Loss: $L(x, x') = ||x-x'||^2=||x-f'(W'(f(Wx+b))+b')||^2$

![autoencoder](/researchPng/research/autoencoders_2.png)

图 3 说明了从一天的登录/注销活动中提取的几个采样的正常/异常特征向量，其中每个像素代表登录/注销审计数据。一个 6×8 像素的图像表示发送特征向量的归一化值（从 0 到 1）。

对于正常特征向量的情况，前两行分别可视化原始特征向量和重建特征向量。底部两行显示相同的登录/注销特征向量，但用于异常用户行为情况。从图的顶部两行，我们可以观察到法线特征向量看起来非常相似，这与我们假设存在可以表示常见用户行为的基线模型一致。底部两行的模式表明被恶意登录/注销操作污染的特征向量与正常特征向量不同，并且它们的重构形式放大了这种差异。直观地，我们能够通过测量其原始形式和重建形式之间的差异来检测异常特征向量。

![图3](/researchPng/research/autoencoders_result.png)


自编码器的架构设计可以对自动编码器的性能有显着影响 [13]。应考虑以下因素：1) 应使用的总层数，包括输入和输出层 2) 对于每一层，隐藏单元的数量和激活函数的选择，以及 3) 损失函数的选择被最小化。由于我们总共应用了四个自动编码器，四个审计数据类别中的每一个都有一个，因此可以通过为每个自动编码器使用不同数量的层来获得每个数据类别的最佳特征表示。

例如，如图 3 所示，一般每个用户每天只有 2-3 次登录和注销计算机，导致特征向量非常稀疏，而登录和注销的频率是按小时计算的.在这种特殊情况下，正如我们的数值实验将显示的那样，2-3 层足以用于登录/注销自动编码器。

图 3 表明这些特征不像从图像或文本中提取的特征那么复杂，并且其中一些特征具有很强的相关性。因此我们倾向于选择简单的激活函数，例如线性单元。为了最大化正常和异常用户行为之间的可分离性，我们试图使用一种损失函数来惩罚结构差异而不是数值差异

然而，在实践中，一般很难选择一个合适的阈值，尤其是当数据集很大时[19][20]。在我们的例子中，我们使用 top-N 推荐算法 [21] 只生成 top-N 异常行为特征向量。换句话说，每个审计数据检测器使用自己训练的自动编码器对所有特征向量进行重建，按降序对重建错误进行排序，并仅报告前 N 个。最后，将来自四个检测器中每一个的前 N ​​个重构误差组合在一起以做出最终决定。由于每个检测器都关注特定攻击向量的结果，因此组合不同的审计数据检测器以识别内部攻击更有意义。
1
其中 μ 和 σ 分别表示重构误差的均值和标准差，k 对应于检测器索引（k = 1, 2, 3, 4）。 其次，然后将前 N 个归一化重建错误组合在一起，按用户和日期对齐。 当用户没有一个检测器的输入特征向量时，错误率归零值。 然后将平均重建错误计算为恶意分数，对应于每对用户和日期。 最后，再次应用top-N算法以报告具有最大恶意评分的前N对用户和天。 然后，计算机应急响应小组 (CERT) 分析员可以使用此用户日对订购来进一步调查异常行为。

我们将误报率固定在 1% 到 10% 的范围内。图 5 说明了得到的 RoC 曲线，从中我们可以得出结论，我们可以通过仅调查总（组合）活动的 6% 来检测所有攻击（即，当 TPR=100% 时）。随后，我们还可以确定理论是什么 -
对于相同的检测精度，它可以达到的最小误报率。结果表明，通过调查 0.1% 的原始数据集，我们已经能够达到 66.7% 的真阳性率，通过调查 5.6% 的原始数据集，我们可以检测到所有的攻击。这样的结果证明了所提出的检测系统的实际可行性。在实际场景中，这意味着给定的组织每天监视 5000 个用户的行为，并且每个用户每天可能只生成一个事件（特征向量），那么最多只需要 300 个事件由 CERT 人类专家手动调查，这显着减少了分析师的整体认知工作量。 

检测总结：针对四个检测器的前N个输出进行平均加权组合。

# 5. 解决了什么问题（贡献）

# 6. 实验结果

# 7. 如何想到该方法

# 8. 我能否想到该方法

# 9. 创新点是什么

# 10. 如何用于本专业

# 11. 该方案还存在的问题

# 12. 注释
