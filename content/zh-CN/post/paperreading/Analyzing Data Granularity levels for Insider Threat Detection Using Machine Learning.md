---
title: "Analyzing Data Granularity Levels for Insider Threat Detection Using Machine Learning"
date: 2021-09-28T09:24:22+08:00
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
---

# 目录： <!-- omit in toc -->
- [1. 综述翻译](#1-综述翻译)
  - [1.1 发表于](#11-发表于)
- [2. Tag](#2-tag)
- [3. 任务描述](#3-任务描述)
- [4. 方法](#4-方法)
  - [Overview](#overview)
  - [Data Collection and Pre-processing](#data-collection-and-pre-processing)
  - [ML for Data Analytics](#ml-for-data-analytics)
- [5. 解决了什么问题（贡献）](#5-解决了什么问题贡献)
- [6. 实验结果](#6-实验结果)
- [7. 如何想到该方法](#7-如何想到该方法)
- [8. 我能否想到该方法](#8-我能否想到该方法)
- [9. 创新点是什么](#9-创新点是什么)
- [10. 如何用于本专业](#10-如何用于本专业)
- [11. 该方案还存在的问题](#11-该方案还存在的问题)
- [12. 注释](#12-注释)

# 1. 综述翻译

## 1.1 发表于

# 2. Tag

# 3. 任务描述

# 4. 方法

## Overview

恶意行为和内部威胁检测系统的建议方法如图1所示。 系统流程如下：

1) 数据采集：多源数据采集，统一格式存储。两个主要来源是： 
   1) • **用户活动**，例如网络流量、电子邮件、文件日志。 
   2) • **组织结构和用户资料信息**。
2) 数据预处理：对聚合后的数据进行处理，构建表示不同粒度级别的用户活动和个人资料信息的特征向量。
3) 基于构建的特征向量，采用ML算法进行数据分析。
4) 结果以不同的格式呈现，并向系统分析员提供详细的分析。

该系统旨在在安全分析师的参与/监督下进行许多步骤，特别是在初始检测中，其中调查恶意行为和异常活动的早期迹象。人类分析师不仅在分析系统警告和警报方面发挥重要作用，而且在执行必要的操作以在攻击后将系统恢复到“正常”运行方面发挥着重要作用。在这里报告的工作中，我们假设 CERT 提供的基准数据集（第 IV-A 部分）用于评估图 1 的数据分析组件的特定目的。具体来说，我们有兴趣评估在有限基础上训练的 ML 算法检测未知恶意内部人员的真相。为此，采用监督学习算法从获得的关于恶意/正常用户行为的知识（基本事实）中学习。然后，我们探索学习到的解决方案在检测未知恶意内部案例时能够泛化的能力如何。使用监督学习的好处是我们不需要假设数据集群总是与不同的行为同义。这可能会导致比无监督学习/异常检测算法 [13]（第 IV-C2 节）更高的精度。

> 采用监督学习??

> 基于用户的检测？“简而言之，我们认为突出恶意用户而不是事件的结果代表了更重要的系统性能衡量标准。”

此外，我们的分析将区分检测到的恶意操作和检测到的恶意用户，两者不一定相同。也就是说，组织内用户角色的多样性会影响所执行操作的数量/类型，包括正常的和恶意的。在许多情况下，用户操作可能会随着时间的推移而变化，并且需要考虑多个上下文，以便处理有关可疑行为的警报 [34]。因此，在这种情况下，高恶意实例检测率可能不一定会转化为检测到所有恶意内部人员。此外，如果将许多不同的正常用户标记为异常，看似很小的误报率可能仍然需要安全分析师的大量关注。简而言之，**我们认为突出恶意用户而不是事件的结果代表了更重要的系统性能衡量标准。**

最后，提出了几种措施，例如每个恶意内部人员的检测延迟，或对每个恶意内部人员警报的支持。通过提供这些措施，我们旨在为安全分析师提供更好的支持，并为所提议的系统在实际场景中的成功应用做出积极贡献。


## Data Collection and Pre-processing

数据收集和预处理对于内部威胁检测尤其重要，而且对于一般的网络安全任务也至关重要。良好的监控程序与足够的数据收集相结合，可以成功应用 ML 技术并支持安全分析师做出正确的决策。从组织环境中收集的数据可能来自各种来源，并且有许多不同的形式 [4]、[35]。本研究假设组织数据收集在两个主要类别中：(i) **活动日志数据**，以及 (ii) **组织结构和用户信息**。第一类数据来自不同的日志系统，例如网络流量捕获、防火墙日志、电子邮件、Web 和文件访问。这些代表通常需要及时收集和处理的实时数据源，以便快速检测和响应恶意和/或异常行为。第二类数据代表背景或上下文数据，可以是员工信息、组织中的角色、与其他用户的关系。在许多情况下，该类别还包含更复杂的数据，例如用户的心理测量和行为模型。为了协助数据处理和特征构建，为组织中的每个用户创建了用户上下文模型。模型由与每个用户相关的辅助信息组成，例如分配的机器、与其他用户的关系、角色、工作时间、允许访问等。基于用户上下文模型，可以从传入的数据中快速有序地创建总结用户行为的特征向量。 

1) 特征提取：从收集到的数据和用户上下文模型中，可以进行特征提取以创建适合训练 ML 算法的数据向量。 首先，给定**聚合条件 c**，例如**持续时间或执行的操作数**，基于用户 id 聚合来自不同来源的数据。 随后，对聚合数据进行特征提取，生成固定长度 N 的数值向量 x_c，也称为数据实例，汇总用户动作。 每个向量都包含用户信息——主要是以数字格式编码的分类数据，用于为 ML 算法提供上下文——以及两种类型的特征：

> 给定聚合条件c，基于用户id聚合来自不同来源的数据。生成固定长度N的数值向量XC。包含频率特征和统计特征。

• **频率特征**，即用户在聚合期间执行的不同类型操作的计数，例如发送的电子邮件数量、下班后访问文件的数量或在共享 PC 上访问的网站数量。
• **统计特征**，即**数据的描述性统计**，例如均值、中位数、标准差。 统计功能中汇总的数据示例包括电子邮件附件大小、文件大小和访问过的网站中的字数。

图 2 展示了在这项工作中使用 CERT 数据集的情况下的特征创建过程。 该过程允许创建由许多细节组成的信息丰富的特征，例如 PC、时间和特定于动作的特征。 图 2 中显示的最多三个连接的信息组合在一起以生成一个特征，例如**共享 PC 上的操作数**、**下班后的 HTTP 下载数**、**已发送电子邮件的平均附件大小**。 因此，构建的功能集本质上是对信息片段的枚举。1 HTTP 和文件功能要求我们在企业环境中定义可能有助于内部威胁检测的网站和文件类别集。 此外，精心设计的用于收集活动信息的分类方案直接有助于保护隐私的用户监控，因为在数据预处理中不会检查用户访问的特定网站和文件及其内容[36]。

2）数据粒度：基于上述数据聚合条件c，提取的特征可以具有不同级别的粒度。我们探讨了 c 的两个主要标准：**持续时间**和**执行的操作数量**。表一根据不同的粒度级别总结了本研究中提取的数据类型。在持续时间的情况下，假设用户活动的三个数据聚合：周、日或会话 [27]，[29]。用户周和用户日数据实例汇总了用户在相应时间段内的活动。这些粗粒度类型的数据提供了一天或一周内行为的高级概述，其特征计数高于会话和子会话数据。因此，它们可以通过减少提取的数据实例的数量来潜在地加速学习过程。另一方面，用户会话数据点通过捕获用户在 PC 上的操作，**从登录到相应的注销，提供更高的数据保真度**；或从一次登录到下一次登录。基于会话的数据可用于隔离恶意操作，因为恶意用户倾向于在特定会话中执行恶意操作，而同一天或同一周的其他会话可能仍然正常 [8]。此外，由于会话的持续时间通常比一天短得多，因此当检测到恶意实例时，这种数据类型还可以允许更快的系统响应。

> 三个数据聚合。周、日或会话。这些粗粒度类型的数据提供了一天或一周内行为的高级概述，其特征计数高于会话和子会话数据。另一方面，用户会话数据点通过捕获用户在 PC 上的操作，从登录到相应的注销，提供更高的数据保真度；或从一次登录到下一次登录。基于会话的数据可用于隔离恶意操作，因为恶意用户倾向于在特定会话中执行恶意操作，而同一天或同一周的其他会话可能仍然正常 
> 这句话的意思就是会话比周、日更合适。

由于会话可能持续数小时并包含数百个操作，因此我们进一步探索了每个数据实例中汇总的数据量与对恶意行为的潜在系统响应时间之间的平衡。这是通过使用持续时间和执行的动作数量作为将用​​户会话数据实例分成子会话数据实例的标准来完成的。通过这种方式，我们可以控制嵌入到每个数据实例中的信息量。因此，如果基于 ML 的系统能够成功地从短暂的子会话数据中学习以检测恶意行为，则系统的响应时间可能会得到改善。如表 I 所示，根据持续时间，从用户在 PC 上的会话开始时间起每 i 小时创建一个用户子会话 Ti 数据实例。类似地，从登录操作开始，用户在 PC 上的每 j 个操作后都会创建一个用户子会话 Nj 数据实例。 i 和 j 越小，数据的保真度越高，但实例中汇总的用户活动信息量也越少。在第 IV-A 节中进行了实证分析，以确定 CERT 数据集的 i 和 j 的最合适值。

> 为控制会话包括在里面的时间，来控制信息量。控制i，j（每i个小时，每j个动作的session量）。

> 总结下，特征提取，提取了两方面的特征，统计特征（发的邮件里的文本数）和频率特征（访问次数）。
> 提取了两方面的特征，用户信息，和组织结构信息。属于哪一组。

> 有这个用户的信息组。就是这个人的信息属于同一个组。需要查看一个组的用户的操作是否相似。
## ML for Data Analytics

在本研究中，采用了以下四种众所周知且广泛使用的 ML 算法：逻辑回归、随机森林、神经网络和 XGBoost [7]、[13]、[37]、[38]。 下面给出了算法的简要描述，而更详细的描述可以在 [39] 中找到。

# 5. 解决了什么问题（贡献）

# 6. 实验结果

从受限的数据中进行训练（400个正常、恶意用户前37周，50%的时间）。

表 IV 和图 6 说明了 IF 实现的结果。结果清楚地表明，当标签信息（尽管有限）可用于训练 ML 算法时，监督学习中的引导搜索将实现卓越的性能，尤其是在 FPR 非常低的情况下。无监督学习算法不够好。

> 有监督可以更好的进行学习，哪怕是使用对比学习的自学习。

> 基于用户的报告效果更好。而且更贴近实际需求。当用户有周被报告为异常的话，就判定其为异常。

> 根据图10，EANOC 这些特征也对分类有帮助。根据图10定义部分特征。

每个版本都表征一个拥有 1000 到 4000 名员工的组织。这项工作中使用的数据集 (CERT r5.2) 的 5.2 版模拟了一个在 18 个月内拥有 2000 名员工的组织。 CERT r5.2 由用户活动日志组成，分类如下：登录/注销、电子邮件、Web、文件和 U 盘连接，以及组织结构和用户信息。

CERT r5.2 中的每个恶意内部人员都属于四种流行的内部人员威胁场景之一：**数据泄露（场景 1）、知识产权盗窃（场景 2、4）到 IT 破坏（场景 3）。**

> 有四个场景实例。


图 3 显示了用户会话数据按动作数量、每个会话的持续时间以及两个特征之间的关系的分布。现在很明显，大多数用户会话数据的动作少于 300 个，超过一半的会话少于 100 个动作。因此，我们得出结论 j = {25, 50} 用于提取 usersubsession Nj 数据。另一方面，会话时长更接近于均匀分布，很大一部分持续时间超过 8 小时。此外，如图 3 所示，许多少于 50 个动作的会话可能会持续超过 10 个小时。因此，我们探索 i = {2, 4} 的值以按时间提取子会话数据。表 II 概述了数据类型以及正常和恶意用户的数量。可以看出，数据分布极度偏斜，恶意内部人员相关数据分别仅占用户周、用户日和用户会话数据的 0.39%、0.19% 和 0.18%。在子会话数据上，这个数字更小，从 0.09% 到 0.15% 不等。此外，在检查不同的内部威胁情景时，似乎存在不同的模式。场景 3（与 IT 破坏相关的恶意行为）拥有最少的用户和数据实例。另一方面，场景 2 和场景 4 中的恶意行为（针对不同类型的知识产权盗窃行为）跨越了很长的时间——8 周（超过 240 个恶意用户周数据实例/30 个用户）。这可能表明恶意内部人员试图通过长时间执行恶意操作来避免检测。然而，当考虑单个恶意会话时，场景 2 和 4 之间会出现不同的特征。虽然场景 4 的几乎所有单个恶意会话都很短（少于 2 小时或 25 个操作），但很大一部分场景 2 会话超过 50 个操作并且跨度超过 4 小时。

> 这里明显突出了会话时间、周、日都会展现出不同的检测效果，会从不同的方面对恶意行为进行检测。

In this work, our aim is to obtain a realistic estimation of the proposed system’s performance on real-world networked systems, based on scenarios characterized by limitations to the amount of ground truth data available for training the ML algorithms.

> 以真实世界的ground-truth.

具体来说，在现实环境中，用于训练检测系统的标记（地面实况）数据很少。因此，真实情况只能从有限的一组经过验证的用户那里获得，而其他人的行为通常是未知的 [14]、[48]。为了模拟这种情况，我们假设了一个主要配置——即之后的现实条件——在给定的时间段内仅从有限的一组用户那里获得真实情况。因此，用于训练 ML 算法的真实数据仅限于 400 个识别出的“正常”和“恶意”用户（组织中的 2000 个用户）的数据，基于前 37 周 – 50% 的时间段数据集覆盖。根据用户数量，这允许 ML 算法从代表 18% 的“正常”用户和 34% 的恶意内部人员的数据中学习。值得注意的是，从检测器的角度来看，训练数据中的“正常”用户只能保证在前 37 周是良性的，而在测试周后期，他们可能会也可能不会变成“恶意”。此外，我们通过呈现仅从未知用户（即在前 37 周内未执行任何恶意操作的用户）获得的结果，进一步确保实验的真实性。通过从系统性能指标中排除已知的恶意用户，即训练数据中包含恶意行为的用户，我们认为所进行的评估反映了现实生活中的情况以及网络安全分析师的兴趣 [34]。评估结果是从一系列实验中获得的，其中每个设置（一种数据类型的 ML 算法）随机重复 20 次。

在第一个实验中，为了显示传统 ML 应用程序与现实世界网络安全情况之间的对比，我们将上述现实设置与理想（传统）设置进行比较，其中使用整个数据集中随机 50% 的数据进行训练ML 算法。这是在三个数据粒度级别完成的：用户周、用户日和用户会话。

第二个实验在所有上述数据粒度级别的现实设置中评估 ML 算法，以获得基于实例和基于用户的详细结果。对数据集中提供的每个内部威胁场景的结果进行详细分析。此外，在 CERT r5.2 上训练的模型还用于针对其他版本的 CERT 内部数据进行测试，以探索训练模型在新环境/未知环境下的表现的泛化（不同版本的 CERT 数据模拟不同的组织）。


学习算法——有监督与无监督：虽然这项工作的重点是使用 ML 算法从有限数量的标记数据中学习以检测看不见的恶意内部人员，但在本节中，我们将在实际训练条件下比较所使用的 ML 算法和隔离森林的性能(IF) [53]，一种突出的无监督学习方法，最近已在许多网络异常检测工作中使用 [54]。 IF 假设异常数据实例比正常实例更容易与数据的其余部分隔离，因此到异常实例的相应叶子的路径长度更短。对于训练 IF 模型，针对每种数据类型调整树的数量。根据用于调查标记异常事件的不同可用预算，我们将警告数据实例的三个不同阈值（1%、5% 和 10%）假设为“异常”。表 IV 和图 6 说明了 IF 实现的结果。结果清楚地表明，当标签信息（尽管有限）可用于训练 ML 算法时，监督学习中的引导搜索将实现卓越的性能，特别是在非常低的 FPR 时。

> 有监督学习算法比无监督要好很多。

) 基于实例的结果：基于实例的结果显示在表 V 和图 5 中。总体上一个明显的趋势是 ML 算法的基于实例的性能正在下降（w.r.t. IDR 和 IF1）由于更高的数据粒度级别。具体而言，在以下情况下可以观察到显着差异
在几乎所有情况下比较不同数据粒度级别的基于实例的结果 (IF1)。例如，比较用户周和用户会话之间或用户会话和用户子会话 T2 之间的 RF IF1 都产生 p = 9e−5。图 6 进一步证明了观察结果，其中用户周数据的 AUC 高于用户会话数据。这可以通过嵌入在不同数据类型的每个数据实例中的信息量来解释（参见第 III-B 节），其中粗粒度的数据类型，例如用户周和用户日，涵盖更长的时间段并汇总更多的行为信息，即用户操作，而不是细粒度的数据类型，例如 user-session 和 user-subsession。此外，细粒度数据类型（第 IV-A 部分）中更大的实例计数和更高的不平衡数据分布也可能导致观察到的基于实例的结果的退化。 2) 基于用户的结果：表 V 和图 5 和 7 显示
ML 算法在不同数据粒度级别上基于用户的结果。与在基于实例的结果中观察到的趋势相反，基于用户的结果（UDR、UF1）通常对不同的数据粒度级别更加稳健。除了 XG 算法之外，在大多数情况下，数据类型的度量之间没有大的变化 (>5%)。此外，尽管检测到的恶意内部数据实例的比例相对较低（表 V），但分类器可以学习为大多数恶意内部人员（80% 到 90%）检测至少一个恶意实例。基于用户的结果报告也大大调整了误报率。例如，NN 仅实现了 0.14% 的 IFPR，但在用户会话数据上实现了 3.44% 的 UFPR。这些观察显示了简单地报告每个数据实例而不是每个用户的结果的缺点，前者可能不一定证明检测器检测恶意用户的能力的真实估计。在实践中，似乎基于用户的指标
证明使用细粒度数据类型的合理性，例如用户会话

> 这个想法是很有用的，基于用户的实例的检测要比基于操作的检测更容易检测出异常。

问题：怎么基于用户进行检测的？

用户子会话数据没有优于用户会话数据。

问题：用户会话数据是怎么构建的？

通常在所有数据类型上，只有场景 2 中的内部人员被遗漏。值得注意的是，虽然 UDR 和 UFPR 与在 CERT r5.2 上观察到的相似，但鉴于 CERT r5.1 中恶意用户的数量较少，UPr 和 UF1 较低。另一方面，CERT r6.2 似乎提出了新的挑战，可能是由于不同的组织结构。值得注意的是，未检测到 CERT r6.2（场景 5）中的新内部威胁场景。该场景描述了“因裁员而大量减少的用户将文档上传到 Dropbox，并计划将其用于个人利益”的行为 [33]。这个场景不仅代表了训练模型的一种新的恶意行为，而且与其余四个场景相比，它显示出更少的突兀行为。在数据粒度上，用户会话表现出较低的性能
比来自 CERT r6.2 的其他数据类型。这表明在具有不同用户行为模型的不同组织中，用户数据的会话可能代表不同的操作过程。在这种情况下，更聚合的数据类型（例如用户日和/或用户周）可能会显示出更好的结果。总体而言，本节中的结果表明训练的模型对于组织中的内部威胁检测，只能用作不同环境中的初始检测步骤。特定模型需要从头开始重新训练或从现有模型发展而来以获得更高的准确性。此外，需要异常检测来识别新的恶意行为。

> 用户会话对于新的恶意行为效果不好。针对不同的恶意行为需要分别设立模型进行检测。

在这项研究中，提出了一种基于机器学习的系统，用于组织网络系统中的内部威胁检测。该工作对四种不同的 ML 算法（LR、NN、RF 和 XG）在多个数据粒度级别、有限的真实情况和不同的训练场景进行了基准测试，以支持网络安全分析师检测未知数据中的恶意内部行为。评估结果表明，所提出的系统能够成功地从有限的训练数据中学习并推广以检测具有恶意行为的新用户。该系统实现了很高的检测率和精度，特别是
当考虑基于用户的结果时。在四种 ML 算法中，RF 明显优于图 10. 用户会话数据中的特征重要性。表九
其他作品的结果
其他算法，在大多数情况下，它实现了高检测性能和 F1-score 以及低误报率。另一方面，NN 允许稍微更好的内部威胁检测性能，但代价是更高的误报率。在数据粒度上，用户会话数据提供高恶意内部检测率和最小延迟。另一方面，用户日数据显示在检测特定内部威胁场景（即场景 2 - 知识产权盗窃）方面的性能略好。此外，当应用于不同组织的数据时，它似乎更具普遍性。未来的工作将调查时间信息的使用
在用户操作中。具体来说，这项工作中的所有模型都提供了基于仅限于单个示例的状态描述的标签。使模型能够看到多个示例或保留状态（循环连接）有可能使模型成为可能
做出非马尔可夫决策。

# 7. 如何想到该方法

# 8. 我能否想到该方法

# 9. 创新点是什么

# 10. 如何用于本专业

# 11. 该方案还存在的问题

# 12. 注释