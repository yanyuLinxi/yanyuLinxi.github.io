---
title: "DeepReflect"
date: 2022-02-14T21:09:03+08:00
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
  - [特征](#特征)
- [5. 解决了什么问题（贡献）](#5-解决了什么问题贡献)
- [6. 实验结果](#6-实验结果)
- [7. 如何想到该方法](#7-如何想到该方法)
- [8. 我能否想到该方法](#8-我能否想到该方法)
- [9. 创新点是什么](#9-创新点是什么)
- [10. 如何用于本专业](#10-如何用于本专业)
- [11. 该方案还存在的问题](#11-该方案还存在的问题)
- [12. 注释](#12-注释)

# 1. 综述翻译
深度学习继续在**恶意软件分类**方面显示出可喜的结果。然而，为了识别关键的恶意行为，恶意软件分析师仍然需要使用静态分析工具对未知的恶意软件二进制文件进行逆向工程，这可能需要数小时。尽管机器学习可用于帮助识别二进制文件的重要部分，但由于获取足够大的标记数据集的费用，有监督的方法是不切实际的。为了提高**静态（或手动）逆向工程的生产力**，我们提出了 DEEPREFLECT：**一种用于在**恶意二进制文件中**本地化**和**识别恶意软件组件**的工具。为了定位恶意软件组件，我们以一种新颖的方式使用无监督深度神经网络，并通过**半监督聚类分析对组件进行分类**，分析师在日常工作流程中逐步提供标签。该工具是实用的，因为它不需要数据标记来训练定位模型，并且需要最小/无创标记来逐步训练分类器。在我们对超过 26k 的五位恶意软件分析师的评估中在恶意软件样本中，我们发现 DEEPREFLECT 平均可将分析师逆向工程所需的功能数量减少 85%。我们的方法还检测到 80% 的恶意软件组件，而使用基于签名的工具 (CAPA) 时为 43%。此外，使用我们提出的自动编码器，DEEPREFLECT 比 SHAP（一种 AI 解释工具）表现更好。这很重要，因为 SHAP 是最先进的方法，需要一个标记的数据集，而自动编码器不需要。
## 1.1 发表于
 USENIX CCF A 2021
# 2. Tag

# 3. 任务描述

# 4. 方法

DEEPREFLECT 不做这样的假设，而是通过控制流图 (CFG) 功能和 API 调用的组合来识别这些相同的行为。 DEEPREFLECT 的工作原理是了解良性二进制功能的正常外观。因此，任何异常都表明这些功能不会出现在良性二进制文件中，并且可用于促进恶意行为。

DEEPREFLECT 的目标是识别恶意软件二进制文件中的恶意功能。在实践中，它**通过定位异常的基本块**（感兴趣的区域 - RoI）来识别可能是恶意的功能。然后，分析师必须确定这些功能是否表现出恶意或良性行为。我们的流程中有两个主要步骤，如图 2 所示：（1）**RoI 检测**和（2）**RoI 注释**。 RoI 检测是使用自动编码器执行的，而注释是通过对每个函数的所有 RoI 进行聚类并标记这些聚类来执行的。术语。首先，我们定义“恶意行为”的含义。我们**基于识别恶意软件源代码的核心组件**（例如，拒绝服务功能、垃圾邮件功能、键盘记录功能、命令和控制 (C&C) 功能、利用远程服务等）来生成我们的基本事实。这些很容易被 **MITRE ATT&CK 框架** [9] 描述，该框架旨在标准化这些术语和行为描述。然而，当对我们的评估恶意软件二进制文件（即野生恶意软件二进制文件）进行静态逆向工程时，我们有时无法确定将观察到的低级功能归因于这些高级描述。例如，恶意软件可能出于多种不同原因修改注册表项（其中许多可以由 MITRE 描述），但有时很难确定哪个注册表项被修改是出于什么原因，因此只能松散地标记为“防御规避：修改注册表”在 MITRE。甚至像 CAPA [3] 这样的现代工具也可以识别这些类型的模糊标签。因此，在我们的评估中，**我们将“恶意行为”表示为可以由 MITRE 框架描述的功能**。

**投资回报率检测**。检测的目标是自动识别恶意软件二进制文件中的恶意区域。例如，我们希望检测 C&C 逻辑的位置，而不是检测该逻辑的特定组件（例如，网络 API 调用 connect()、send() 和 recv()）。 RoI 检测的优势在于，分析师可以快速定位到负责启动和操作其恶意行为的特定代码区域。之前的工作只专注于创建临时签名，这些签名只是将二进制文件识别为恶意软件或仅基于 API 调用的某些功能。这对于分析师扩展他们的工作特别有帮助（即，不单独依赖手动逆向工程和领域专业知识）。投资回报率注释。注释的目标是自动标记包含 RoI 的函数的行为。换句话说，**我们管道的这一部分识别了这个恶意功能正在做什么**。使这种标签对分析师的工作流程无干扰且可扩展是至关重要的。分析师为标记集群执行的初始工作是**长尾分布**。也就是说，前期工作量相对较大，但随着他们继续标记每个集群，工作量会减少。此过程的优点很简单：它为分析人员提供了一种自动生成有关未见过样本的报告和见解的方法。例如，如果恶意软件样本的变体包含与以前的恶意软件样本相似的逻辑（但对于分析师来说看起来不同，以至于不熟悉），我们的工具为他们提供了一种更快实现这一点的方法。

## 特征
当给定一个二进制样本时，我们提取特征以将样本总结为 x。在先前的恶意软件检测工作中使用了许多静态特征（例如，代码段熵、导入的 API 调用等）[29、35、53、61、63]。
然而，为了在二进制文件中定位恶意行为，我们的特征必须一对一地映射回原始样本。因此，**我们将每个二进制表示为一个 m×c 矩阵**，该矩阵使用 c 特征捕获前 m 个基本块，以总结它们的每个活动。基本块通常是一系列以控制转移指令结束的指令。当然，根据反汇编程序的不同，基本块的表示方式可能有所不同，因此这种严格的定义可能并不适用于所有静态恶意软件分析系统。我们的功能灵感来自先前作品中的功能，
即**属性控制流图（ACFG）特征**[23, 75]。在这些作品中选择 ACFG 特征来执行二进制相似性是因为它们**假设这些特征（由结构和数字 CFG 特征组成）**将在多个平台和编译器之间保持一致。虽然可以说我们的目标是相似的（即识别二进制文件之间的异同），但我们专门为研究恶意软件定制了这些功能。特别是，我们为自动编码器选择了我们的功能，以捕获更高级别的行为。我们的特征包括每个基本块中指令类型的计数（为 ACFG 特征提取的更详细的形式）、CFG 的结构特征和 API 调用的类别（已用于总结恶意软件程序行为 [18]） .在 DEEPREFLECT 中，**我们将 m 设置为前 20k 个基本块。**
我们选择这个是因为我们 95% 的数据集样本有 20k 或更少的基本块。**我们将 c 设置为 18 个特征**，将每个基本块总结如下：

**结构特征**。我们使用的结构特征是每个基本块的后代数量和中介分数。这些特征可以表示通常用于网络通信（例如，连接、发送、接收）和文件加密（例如，查找文件、打开、读取、加密、写入、关闭）等操作的控制流结构。图 6. 算术指令中可以找到来自实际恶意软件样本的此功能示例。我们使用的算术指令功能是每个基本块中包含的“基本数学”、“逻辑运算”和“位移”指令的数量。这些特征可用于表示如何为更高级别的行为执行数学运算。它们说明了数字是如何与函数交互的（例如，加密函数可能包括许多异或指令，混淆函数可能包括逻辑和位移操作的组合等）。我们从英特尔架构软件开发人员手册 [26] 中检索了这些说明。此外，我们提供了一个恶意软件样本示例，展示了图 9 中的这些类型的功能。
**转移说明**。我们使用的传输指令特征是每个基本块内的“堆栈操作”、“寄存器操作”和“端口操作”指令的数量。这些特征可用于表示如何为更高级别的行为执行传输操作。
它们说明了提供给函数的参数（以及函数调用的返回值）如何与该函数中的其余数据交互。它可能表示复杂的逻辑和数据操作（例如，去混淆/解密可能涉及更多与移动相关的指令，而 C&C 逻辑将涉及更多与堆栈相关的指令，因为它调用更多的内部/外部函数）。我们同样从英特尔架构软件开发人员手册 [26] 中检索了这些说明。
**API 调用类别**。我们使用的API调用特性是“文件系统”、“注册表”、“网络”、“DLL”、“对象”、“进程”、“服务”、“同步”、“系统信息”和“时间”的数量" 每个基本块中的相关 API 调用。这些类别的灵感来自恶意软件聚类的先前工作 [18]。这些功能可用于表示执行恶意活动所需的高级库操作，例如网络通信和文件系统、注册表和进程操作。由于这些直接代表高级行为，因此它们对于理解函数的整体行为至关重要。在图 6 和图 8 中可以找到利用这些不同调用类型来执行不同行为的恶意软件功能示例。

我们认为这些功能比经典的 ACFG 功能更适合恶意软件，因为 (1) 它们包含在先前工作中用于恶意软件检测的 API 调用，(2) 指令类别更细粒度，允许在每个基本功能中包含更多上下文 块（如前所述），并且（3）它们不依赖于太容易受到规避攻击的字符串[77]。 当然，给定一个有动机的对手，任何机器学习模型都可能受到攻击并被诱骗产生不正确和意外的输出。 虽然我们的特征和模型也不例外，但我们认为它们足以产生一个可靠的模型（即，它的行为符合预期）并使其变得足够困难，以至于对手必须广泛工作才能产生误导性输入（ 如第 4.7 节所示）。 有关针对我们系统的潜在攻击的讨论，请参阅第 5 节。

# 5. 解决了什么问题（贡献）

# 6. 实验结果

# 7. 如何想到该方法

# 8. 我能否想到该方法

# 9. 创新点是什么

# 10. 如何用于本专业

# 11. 该方案还存在的问题

# 12. 注释