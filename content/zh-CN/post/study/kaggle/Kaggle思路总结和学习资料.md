---
title: "Kaggle记录总结"
date: 2021-11-05T09:22:40+08:00
tags : [

]
categories : [

]
series : []
aliases : []
draft: false
---
# 学习路线

kaggle要怎么学？
1. kaggle相关技术。当空闲时确定一个kaggle技术进行学习
2. kaggle比赛总结。
3. kaggle比赛尝试。

# kaggle资料

1. Kaggle 竞赛复盘汇总：
   1. https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzIwNDA5NDYzNA==&action=getalbum&album_id=1380279189986787330&scene=173&from_msgid=2247495639&from_itemidx=1&count=3&nolastread=1#wechat_redirect
2. 经验贴
   1. https://zhuanlan.zhihu.com/p/25742261

# 一般流程总结

流程：
1. 首先最开始的时候对数据进行处理：
   1. 将数据处理成pandas（详细学习使用pandas）
   2. 查看是否有NAN值
   3. 查看是否有异常值
   4. 查看数据的众数
   5. 画图看数据的分布。使用log查看分布差异较大的数。
   6. 查看数据和label的相关性 // 重要，因为数据和label紧密相关，就应该好好对待。
2. 针对不同的数据使用不同的算法：
   1. 特征数据：
      1. 变换为图像，然后使用CV相关思路。1d CNN, Resnet 1d等
   2. 文本数据
      1. 使用bert对数据进行预训练。
         1. 预训练思路有很多，包括使用masked在文本上微调。
         2. 或者使用文本分类，直接运算。
      2. 使用tf-idf+svd分析文本中的词频。
      3. 使用ldm对文本主题进行分析。
   3. 归一化处理
      1. 很多树模型不需要归一化，但是神经网络模型大多必需归一化。归一化也有很多，高斯归一化等等，了解他们之间的差异。
3. 然后快速确定一个baseline
   1. 根据评分公式计算评分。方便后面评价模型
   2. 对数据进行训练集、测试集、验证集的分类。
      1. 不要觉得这样分类，减少了数据集会影响分类，其实不是的。可以帮助前期自己对模型的验证。
   3. 常用的树模型：lgbm、catboost、xgboost。等快速的api可以帮助快速出一个api
   4. 常用的神经网络模型。MLP等。
   5. 使用常用的ML框架：Pycaret等。
4. 在baseline上进行改进
   1. 前期脑洞大开，后期小心谨慎
      1. 包括ms等方法只能提升微小且不可忽略的进步，但不能依靠这个就大幅度增长分数。前期必须要脑洞大开。后期必须小心谨慎
   2. 双塔模型。
      1. 双塔最初用在推荐系统上，将人的行为特征和商品的行为特征进行匹配。在这里我们可以分别使用不同的模型对不同类型的特征进行建模。这是十分重要的。不同类型的数据显然不应该放在一起进行训练、测试。
   3. 对特征进行重新提取、筛选。
   4. 伪标签技术。
      1. 使用正负置信度为0.9-0.99的标签二次加入训练
      2. 使用所有标签加入训练，但是为伪标签使用不同的权重矩阵。权重取决于它们的loss函数。
5. 后期优化：
   1. 使用meta_stacking对模型进行搭建。
      1. 这个时候可以用上之前的验证集了。使用验证集训练元学习器。
   2. 对选定的模型进行调参。使用GridSearch或者使用贝叶斯调参
6. 整体注意事项
   1. 需要动手去写的东西并不多，更多的是思路。题目一样的，解法一样，如何取得更好的分数呢？
   2. 数据特征往往很重要，是训练的基石。
   3. 不要全身心投入去做一件事。多件事情交叉，让自己的思路打开。
   4. 不要在程序开始就进行优化。边写脚本，边对模块进行集成。在写模块时，尽量和现有的框架的api进行匹配，减少记忆负担。对看到比较好的方法进行记录。




Notes:
1. 学好pandas
2. 学好seaborn
3. 学好bert模型。对transform系统的学习，能够手撸代码。
4. 以后学习不能不求甚解。对不了解的一定要了解清楚。刨根问底。如果一个知识点足够重要，就开一个md专门写。
5. 多少数据维度是大维度？心里没概念。多看看别人的经验贴，总结能够明白的信息。总结不能明白的信息。要多多调参。


失败总结经验：
1. bert没用熟，很多框架第一次上手，完全不知道怎么弄。
2. 不清楚nn网络能有这么大的效果。
3. 以为不是靠调参解决的，实际上就是靠调参解决的。
4. 调参经验不足。就是经验太少。
5. 多少数据维度是大维度？心里没概念。多看看别人的经验贴，总结能够明白的信息。总结不能明白的信息。


# 工具记录

1. 时序工具。
https://mp.weixin.qq.com/s/sO-Od9x_QH27zJOg6e_FKg