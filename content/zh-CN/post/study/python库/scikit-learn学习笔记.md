---
title: "Scikit Learn学习笔记"
date: 2021-09-28T20:18:10+08:00
tags : [
   "python相关库学习",
   "机器学习相关库",
]
categories : [
   "学习"
]
series : []
aliases : []
draft: false
---

- [概览](#概览)
  - [整体框架](#整体框架)
    - [unsupervised](#unsupervised)
      - [unsupervised methods](#unsupervised-methods)
    - [cluster](#cluster)
  - [API](#api)
  - [validation API](#validation-api)
  - [metrics](#metrics)
  - [models](#models)
  - [embedding](#embedding)
  - [Cluster Overview](#cluster-overview)
  - [Unsupervised dimensionality reduction](#unsupervised-dimensionality-reduction)
    - [PCA](#pca)
    - [Random projections](#random-projections)
      - [johnson_lindenstrauss_min_dim](#johnson_lindenstrauss_min_dim)
      - [GaussianRandomProjection](#gaussianrandomprojection)
      - [SparseRandomProjection](#sparserandomprojection)
    - [Feature agglomeration](#feature-agglomeration)

# 概览

## 整体框架

```python
# set numpy seed. when it comes to random functions, please leave a function to set seed.

# load data
x, y = sklearn.data

# train test data split.

# create model entity
model = sklearn.model(params)

# model train
model.fit(x, y)  # which contains the train process.

# model test
results = model.predict(test) # predict the test result

# metrics
results_proba = model.predict_proba(test) # output the probablity of the each label.

models.score() # scores are between 0 and 1, with a larger score indicating a better fit.

# for unsupervised method
model.transform() # transform new data into new basis

model.fit_transform() # performs a fit and a transform on the same input data.

model.predict()

```

### unsupervised

est = KMeans(4)
est.fit(X)
out = est.predict(X)

or est.fit_predict(x)

#### unsupervised methods
1. Isolation Forest
   1. params
      1. n_jobs = -1 means all cpu.
      2. contamination means the amount of contamination of the dataset. it means the threshold of whole data.
      3. n_estimators: the number of base estimators.
      4. max_samples: the number of samples to draw from X to train **each estimator**
   2. function:
      1. decision_function(X). 返回样本的异常评分。
      2. score_samples(X) return abnormal score of samples.The lower, the more abnormal.




问题：
1. 无监督的 fit_predict 和 fit 后 predict有什么区别？
   1. 无监督学习基本使用fit_predict。
   2. 也不是，fit_predict如其名字，就是先预测。然后进行predict。我们按照神经网络中的做法。8预测，2个predict。
2. max_samples的作用

### cluster

clust.cluster_centers_ 是簇类的中心

## API

## validation API

1. sklearn.metrics.confusion_matrix(y_true, y_pred, *, labels=None, sample_weight=None, normalize=None)
   1. Compute confusion matrix to evaluate the accuracy of a classification.
   2. y_true = [2, 0, 2, 2, 0, 1]
        >>> y_pred = [0, 0, 2, 2, 0, 2]
        >>> confusion_matrix(y_true, y_pred)
        array([[2, 0, 0],
            [0, 0, 1],
            [1, 0, 2]])
2. sklearn.model_selection.train_test_split(*arrays, test_size=None, train_size=None, random_state=None, shuffle=True, stratify=None)[source]
   1. Split arrays or matrices into random train and test subsets
   2. random_state保证每次划分结果都一样。
3. model_selection.cross_val_score交叉验证评估分数
   1. 通过不停将测试组和训练组分组来评估模型分数。
   2. 参数cv表示数据折叠数量。
   3. 返回分数。
4. model_selection.validation_curve
   1. cv是交叉验证的值。
   2. 确定不同参数值的训练和测试分数。
5. learning_curve
   1. 确定不同训练集大小的交叉验证训练和测试分数。
6. GridSearchCV使用网格搜索模型指定参数。

## metrics
1. accuracy_score
   1. Accuracy classification score. In multilabel classification, this function computes subset accuracy: the set of labels predicted for a sample must exactly match the corresponding set of labels in y_true.

## models

1. model select
   1. ![tough luck](/researchPng/research/modelSelectSklearn.png)
2. svm
   1. sklearn.svm import SVC
   2. clf = SVC(kernel="linear")
   3. clf = SVC(kernel="rbf")
3. random forest
   1. sklearn.tree import DecisionTreeClassifer()
   2. sklearn.ensemble.RandomForestClassifier
   3. sklearn.ensemble.RandomForestRegressor
   4. sklearn.ensemble.RandomTreesEmbedding  无监督随机森林
   5. clf = rfclf(n_estimators=100, random_state=0)
4. cluster
   1. KMeans
      1. fit(x)计算k均值聚类
      2. fit_predict(x)计算样本的聚类中心，并预测聚类索引。
5. 异常检测：
   1. sklearn.ensemble.IsolationForest
   2. sklearn.covariance.EllipticEnvelope
   3. sklearn.svm.OneClassSVM
   4. sklearn.neighbors.LocalOutlierFactor
   5. 

## embedding
1. manifold:
   1. sklearn.manifold.Isomap()
   2. Isomap Embedding. 用来做embedding的。将特征映射到2维后，进行画图。
   3. Non-linear dimensionality reduction through Isometric Mapping

mainfold就是来做映射embedding的

2. make_blobs
   1. 函数是为聚类产生数据集 产生一个数据集和相应的标签





## Cluster Overview

https://scikit-learn.org/stable/modules/clustering.html
中文:
https://sklearn.apachecn.org/docs/master/22.html#k-means

聚类是把相似的对象通过静态分类的方法分成不同的组别或者更多的子集（subset），这样让在同一个子集中的成员对象都有相似的一些属性。

一些常见聚类方法简介：
1. k-means

以空间中的k个点为中心进行聚类。对最靠近它们的对象归类。

2. KNN

一个对象的分类由其邻居的多数表决确定。k个最近邻居中最常见的分类决定赋予了该对象的类别。


## Unsupervised dimensionality reduction

### PCA
使用奇异值分解将data进行线性分解，来将其映射到一个低维的空间。来去除特征之间的相关性。
不支持稀疏输入。输入的数据居中化，但是并没有缩放。

一般来说先标准化后再进行pca分析。

Params
1. n_components:
   1. Number of components to keep. if is not set, n_components=min(n_samples, n_features)
   2. copy bool, True means copy data and transform
   3. whiten bool, when true whitening will remove some information from the transformed signal.会从转换后的信号中去除一些信息。
   4. svd_solver auto full arpack randomized
      1. auto: selected based on X.shape and n_components
      2. full: full SVD
      3. arpack: SVD truncated 
      4. randomized: run randomized SVD
   5. random_state

Attribute:
1. components_
   1. principal axes in feature space. The components are soted by explained_variance_ 具有最大方差的成分
2. explained_variance_  保留的n个成分和各自的方差百分比
3. n_components_ 保留的成分个数n
   
API:
1. fit
2. transform(X)
   1. 将数据X转换为降维的数据。模型fit后，对新输入的数据，可以使用transform来降维。

### Random projections

#### johnson_lindenstrauss_min_dim
JL随即投影
API： https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.johnson_lindenstrauss_min_dim.html#sklearn.random_projection.johnson_lindenstrauss_min_dim

原理解释：
通俗版JL引理： 塞下N个向量，只需要$O(logN)$维空间。
高维空间中任意两个向量几乎都是垂直的
从$N(0, 1/n)$采样出来的$n*n$矩阵几乎是一个正交矩阵
Params:
1. n_samples:
   1. Number of samples
2. eps:
   1. Maximu distortion rate

Return:
1. n_components:
   1. 最小的组件来保证很好的最小大小来保守估计随即子空间的最小大小。保证随机投影的有界失真。


#### GaussianRandomProjection
高斯随机投影

params:
1. n_components 目标投影空间的维度。
   1. 可以根据样本数量和johnson-Lindenstrauss引理给出的界限自动调整。嵌入的质量由参数eps控制
2. eps
   1. 当n_components设置为“自动”时，根据 Johnson-Lindenstrauss 引理控制嵌入质量的参数。
   2. eps 默认0.1 越小则损失的越少。最终需要的特征数量越多。
3. random_state

Attrs:
1. n_components_:
   1. 具体组件数。
2. 其他具体看官方

API：
1. fit
2. transform
3. get_params 获取参数保存
4. set_params 设置参数。

#### SparseRandomProjection
稀疏随机投影随机矩阵

params:
1. n_components 同上
2. density:
   1. auto the value is set as recommended
3. eps 
   1. Parameter to control the quality of the embedding according to the Johnson-Lindenstrauss lemma when n_components is set to ‘auto’. 
4. dense_output
   1. if True will output dense output even input is sparse.
5. random_state

attr:
1. n_components_
2. components_
   1. Random matrix used for the projection. Sparse matrix will be of CSR format.

Api:
1. 同上。

### Feature agglomeration