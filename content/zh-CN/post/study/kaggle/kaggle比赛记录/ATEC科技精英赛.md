---
title: "ATEC科技精英赛"
date: 2021-10-20T15:25:35+08:00
tags : [

]
categories : [

]
series : []
aliases : []
draft: false
---

# 结束复盘

2021 ATEC科技精英赛（网络欺诈举报定性）比赛分享 - 机器学习小谈的文章 - 知乎
https://zhuanlan.zhihu.com/p/434432485
https://jishuin.proginn.com/p/763bfbd6d31e
# 比赛题目

第一道题：

赛题从当前社会中高发的电信网络欺诈识别场景入手，提供模拟的“用户”投诉欺诈信息，要求选手识别投诉中的欺诈风险。



本赛道将选取工业应用中常见的、由于“数据源差异”、“数据维度特征缺失”而导致的、模型应用困难的问题， 考察AI模型如何通过多源数据的有效应用以及半监督学习技术，实现有限数据下的模型决策，从而思考如何减少AI对数据依赖的问题。 赛题从当前社会中高发的电信网络欺诈识别场景入手，提供模拟的“用户”投诉欺诈信息，要求选手识别投诉中的欺诈风险。



11.5 10am 截止。从现在开始满打满算15天。

官方网址: https://www.atecup.cn/competitionIntroduction

第一道题网址：https://www.atecup.cn/trackDetail/1





## 评分



参赛选手提交模型并对榜单数据进行打分（对样本进行欺诈概率预测），后台通过对打 分结果测算出精确率(Precision)、召回率(Recall)曲线，从中推算出：到达精确率为90% 的模型分数阈值下对应的召回率、到达精确率为85%的模型分数阈值下对应的召回率、 到达精确率为80%的模型分数阈值下对应的召回率，三项召回率进行权重分别为0.4、 0.3和0.3加权融合，作为比赛榜单分数。

Score: 0.4 x Recall precision = 90 + 0.3 x Recall precision = 85 + 0.3 x Recall precision = 80



## 服务器使用规则

本地服务器配置及使用规则：CPU:8 core；Memory:16GB；GPU:无；Storage:256G ，不限时使用。

公有池服务器配置及使用规则：模型训练可使用含GPU的公有池服务器资源，训练任务占用资源为CPU:6 core，memory:16g； GPU 1卡(v100), Storage:20G。每次任务最长使用2小时。 每队每周公有池服务器资源使用上限30小时，不作累积。

比赛期间排行榜显示A榜成绩排名，比赛结束后 24小时内 展示B榜成绩排名。比赛结束倒计时24小时内允许提交B榜验证任务；提交后，首次运行成功所得分数即为B榜成绩，之后不能再提交打分任务。如需支持，可联络“咨询中心”。 最终比赛成绩以B榜单为准（如B榜成绩持平，则A榜成绩高者排名在前）。 另，为了鼓励更切合实际应用的模型及方案，A/B榜模型提交的打分任务均将限制在 10分钟内 完成。



关于“周”的说明

线上赛合计21天，每7*24小时为1周，共3周。

第一周 指2021年 10月15日 10:00 AM – 10月22日 10:00 AM

第二周 指2021年 10月22日 10:00 AM – 10月29日 10:00 AM

第三周 指2021年 10月29日 10:00 AM – 11月5日 10:00 AM

A榜验证打分每队每24小时最多 10 次（自2021年10月15日10:00AM起算），剩余次数不做累计。 选手可以通过Jupyternotebook进行编码开发。

## 数据

数据为模拟生成的用户支付宝欺诈投诉举报数据，

1. 标签1代表欺诈案件，
2. 标签0代表非欺诈案件，
3. 标签-1代表未知，
4. 另，测试数据不含-1标签。

数据包含481个特征，其中480个为结构化特征，1个为非结构化的特征。结构化特征包含：欺诈投诉举报案件中主被动双方的相关风控特征，非结构化特征为举报描述信息。无具体特征含义说明。

本赛道所有相关数据（包括但不限于训练数据集）不得以任何形式下载，仅限在主办方提供的本地服务器及含GPU的公有池服务器上、以比赛为目的使用， 违者将被视作“获取未授权数据”，将依照大赛规则，作禁赛处理。

比赛全程只允许使用主办方提供的本地服务器以及含GPU的公有池服务器资源。

如模型训练非必要用到GPU资源，建议优先使用每队不限时的本地服务器资源，以节约每队公有池服务器用时限额。

### 数据分析

1. 第一维为id，"x0"-"x479"为特征。特征不清楚定义。memo_polish为文本特征
   1. id没有重复用来输出这个样本是否是欺诈案件。

## 方案

1. 480维度特征，按列进行归一化。
2. 最后一维度特征首先使用word2vec，编码为特征
3. 对数据特征进行降维：PCA, t-SVD，dimension * 0.8-0.9
4. 特征增强(nlp)概念
5. 使用神经网络。autoencoder。CNN、transformer
6. 使用combination，联合多个模型输出test评分。

神经网络三种方式：
1. 深度神经网络。如Transformer
2. CVPR最好的网络
3. 标签为1的半监督
   1. 用模型推标签
   2. 无标签的自监督学习。

神经网络方法备注:
1. lgbm方法调研

问题：
1. 特征和nlp特征分别处理再合起来
2. 中文文本处理是否需要用TF-IDF这种编码。处理词频的？
3. 中文文本处理的问题
   1. 预训练语料库太大。腾讯的这个有6.3g
   2. 先进行中文分词。然后进行语料库的pretrain导入。
   3. 朋飞学长资料：
      1. 使用jieba进行分词
      2. 使用语料库读取pre-train模型
   4. 对训练集数据的词进行统计，然后给出词列表。然后读取embedding然后存储。
   5. 资源上传大小限制2G
   6. 文本中有中文有数字。
4. 2个小时，是指提交到服务器运行就算时间。不管用不用gpu


## 时间安排

1. 出炉以天为单位的任务安排
2. 每两天对接一次情况



## 任务安排：

- [x] 首先摸清楚数据集的情况
- [x] 摸清楚实验环境、熟悉实验环境。
- [x] 完成初步的神经网络搭建
  - [x] 搭建一个使用gpu训练的方式。
  - [x] 在jupyter 中完成归一化、降维、使用autoencoder。
  - [x] 弄清楚整个gpu的训练流程
  - [x] 再弄清楚整个训练流程、方式。
  - [ ] 调研：
    - [ ] transformer, light transformer
    - [ ] 自监督学习
    - [ ] 训练的trick
    - [ ] 数据测试tta
  - [x] 统计gpu服务器上的数据
- [x] 将整个步骤打通。
- [x] 安装朋飞学长依赖库
- [x] 放到csv中。
  - [x] 统计有没有缺失
  - [x] 如果是使用csv处理的话，肯定不好。因为gpu服务器的数据不行，你不能转成csv再处理。那样比较费时间吧。
- [x] 搭建投票系统
- [ ] 按照lgbm调参指南来训练
  - [ ] 还没发给我
- [ ] 根据评分来计算表格
- [ ] 添加伪标签
- [ ] 过滤掉冗余特征
- [ ] 对过度重合的特征进行筛选

## 登录服务器步骤

### 登录信息
ssh -p  60022 6brdcr99q8@onyiwjcofa-public.bastionhost.aliyuncs.com

passwd zIxH5KfSXl3_XIfjqM

堡垒机
1. 账号
6brdcr99q8
2. 密码
zIxH5KfSXl3_XIfjqM

本地服务器：
账号：
2bv211k1vq
密码
Dko2502eZNGmA0mk0_

Jupyter:
1. 账号
2bv211k1vq
2. 密码
Dko2502eZNGmA0mk0_

#### 登录后常用操作
1. 激活环境
   1. source ~/atec_project/train/your_name_env/bin/activate

#### 提交一次训练
// 将所有文件放在train目录下，通过run.sh来 python train.py
// vtag每次不一样。
cd ~/atec_project
docker build -f Dockerfile.train --network=host -t atec-repo-registry-vpc.cn-beijing.cr.aliyuncs.com/zark/atec-228:vtag .

// 获取临时用户名密码
adabench_cli auth get-docker-token

// 登录
docker login --username=cr_temp_user atec-repo-registry-vpc.cn-beijing.cr.aliyuncs.com

// 提交
docker push atec-repo-registry-vpc.cn-beijing.cr.aliyuncs.com/zark/atec-228:vtag

// 运行任务  -t 指定任务类型，trian为训练，rank_a/rank_b分别刷a/b榜。
adabench_cli task run -i atec-repo-registry-vpc.cn-beijing.cr.aliyuncs.com/zark/atec-228:vtag -t train
// 返回job id

v_ttw_1

// 查看任务
adabench_cli task status -j  

adabench_cli task status -j job_id

// 查看日志
adabench_cli task logs -j  

adabench_cli task logs -j job_id

// 下载产出的模型(只有训练) 只保存24个小时
adabench_cli task download --path /home/2bv211k1vq/atec_project/trained_models -j job_id 
// 解压产出的打包模型
tar xzf ***.tar.gz

// 任务停止
adabench_cli task stop --j [任务id]

=============================================================
// 打榜
// 生成镜像
cp -af ~/atec_project/train/your_name_env ~/atec_project/rank/

docker build -f Dockerfile.rank --network=host -t atec-repo-registry-vpc.cn-beijing.cr.aliyuncs.com/zark/atec-228:vtag .

adabench_cli auth get-docker-token

docker login --username=cr_temp_user atec-repo-registry-vpc.cn-beijing.cr.aliyuncs.com

docker push atec-repo-registry-vpc.cn-beijing.cr.aliyuncs.com/zark/atec-228:vtag

// 运行:rank_a/rank_b分别刷a/b榜。  比赛结束倒计时24小时内允许提交B榜验证任务；提交后，首次运行成功所得分数即为B榜成绩，之后不能再提交打分任务
adabench_cli task run -i atec-repo-registry-vpc.cn-beijing.cr.aliyuncs.com/zark/atec-228:vtag -t rank_a
// 返回job_id

adabench_cli task status -j 
adabench_cli task status -j job_id


#### 第一次提交
{'__metrics': {'code': 0, 'score': 0.5302481389578164, 'msg': 'success'}


### 注意事项

> 赛道一服务器操作指南：
> https://www.atecup.cn/machineGuide

1. 使用jupyter开发的话，记得保持jupyter的环境和your_env_name环境一致。
   1. 每次提交rank的时候复制实验环境到rank
2. 本地ECS机器训练数据集存在于本机的/mnt/atec/train.jsonl
3. 服务器端数据：
   1. 本机
      1. /mnt/atec/train.jsonl
   2. train数据
      1. /home/admin/workspace/job/input/train.jsonl
   3. 模型输出数据存放
      1. /home/admin/workspace/job/output/
   4. 关键信息存放
      1. /home/admin/workspace/job/output/result.json
   5. 测试数据
      1. /home/admin/workspace/job/input/test.jsonl
   6. 预测结果放到：
      1. /home/admin/workspace/job/output/predictions.jsonl
4. 创建docker相关命令
   1. docker images  查看所有镜像
   2. 镜像制作：
      1. cd ~/atec_project
      2. docker build -f Dockerfile.train --network=host -t atec-repo-registry-vpc.cn-beijing.cr.aliyuncs.com/zark/atec-228:v1 .
      3. v1为tag名。每次tag不一样。
   3. docker登录。每次传输前获取镜像密码
      1. adabench_cli auth get-docker-token
      2. 账号：cr_temp_user
      3. docker login --username=cr_temp_user atec-repo-registry-vpc.cn-beijing.cr.aliyuncs.com
   4. 登录后提交：
      1. docker push atec-repo-registry-vpc.cn-beijing.cr.aliyuncs.com/zark/atec-228:v1
5. 大赛触发任务执行：
   1. adabench_cli task run -i atec-repo-registry-vpc.cn-beijing.cr.aliyuncs.com/zark/atec-228:v1 -t train
      1. 会返回一个job_id 就是后面的task id
   2. adabench_cli task status -j job_id
   3. adabench_cli task logs -j job_id
   4. adabench_cli task download -j job_id
6. 训练说明：
   1. 训练和刷榜任务的输出文件必须放置在/home/admin/workspace/job/output/目录下
   2. 如果为刷榜任务：打分的结果文件必须输出到/home/admin/workspace/job/output/predictions.jsonl，平台会使用这个结果文件进行打分
7. 数据集格式：
   1. train
   {"id": "1", "input_feat1": "xx", "label": 0}
   {"id": "2", "input_feat1": "xx", "label": 1}
   1. test
   {"id": "1", "input_feat1": "xx"}
   {"id": "2", "input_feat1": "xx"}
   1. predictions.jsonl
   {"id": "1", "label": 0.4}
   {"id": "2", "label": 0.8}


## 数据统计

1. 首先统计各个数值平均数、众数、最大值、最小值
2. 看看标签为 1 的label长什么样子。


## 相关资料

1. 一些其他比赛的资料。
https://mp.weixin.qq.com/s/vSVhearDrZB3OXW4CXaDGQ



# 我们最后进行赛后自我总结

如果后面有人分享方案的话，时刻保持关注一下，分析一下前三的每个人的方案。

然后我们开始分析下自己的方案进行总结：

流程：
1. 首先最开始的时候对数据进行处理：
   1. 将数据处理成pandas（详细学习使用pandas）
   2. 查看是否有NAN值
   3. 查看是否有异常值
   4. 查看数据的众数
   5. 画图看数据的分布。使用log查看分布差异较大的数。
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
   2. 不要全身心投入去做一件事。多件事情交叉，让自己的思路打开。
   3. 不要在程序开始就进行优化。边写脚本，边对模块进行集成。在写模块时，尽量和现有的框架的api进行匹配，减少记忆负担。对看到比较好的方法进行记录。




Notes:
1. 学好pandas
2. 学好seaborn
3. 学好bert模型。
4. 以后学习不能不求甚解。对不了解的一定要了解清楚。刨根问底。如果一个知识点足够重要，就开一个md专门写。
5. 对transform系统的学习，能够手撸代码。


