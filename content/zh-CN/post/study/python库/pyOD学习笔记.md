---
title: "PyOD学习笔记"
date: 2021-10-09T15:51:08+08:00
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

# 注意

里面有很多需要其他库的神经网络。比如keras。比如tensorflow。为了避免最后太过复杂，这些自己写最好。

# 样例

## 生成污染数据
```python
contamination = 0.1  # percentage of outliers
n_train = 200  # number of training points
n_test = 100  # number of testing points

X_train, y_train, X_test, y_test = generate_data(
    n_train=n_train, n_test=n_test, contamination=contamination)

```
X_train (numpy array of shape (n_train, n_features)) – Training data.

X_test (numpy array of shape (n_test, n_features)) – Test data.

y_train (numpy array of shape (n_train,)) – Training ground truth.

y_test (numpy array of shape (n_test,)) – Test ground truth.


## 一般模式

clf = models()

clf.fit(X_train)

y_train_scores = clf.decision_scores_
y_test_scores = clf.decision_function(X_test)

# API

1. fit(X) 填充检测器。y 在无监督方法中被忽略。用以训练网络
2. decision_function() 输出Y的异常分数
3. predict() 用来拟合 Y
4. predict_proba() 用来输出Y的异常概率。

## attribute

1. decision_scores_ 训练数据的异常值。值越高越不正常。
2. labels_  训练数据的二进制标签。0表示正常。1代表异常。

## 其他API

### metrics
1. from pyod.utils.data import evaluate_print
   1. evaluate_print(clf_name, y_train, y_train_scores)
   2. 输出ROC和precision值。
2. 可视化
   1. visualize(clf_name, X_train, y_train, X_test, y_test, y_train_pred,y_test_pred, show_figure=True, save_figure=False)
   2. 

### combination

1. 四种模型组合 最大值平均，平均值最大。最大值。平均值。
   1. 先获取每一个样本所有点的异常分数
   2. 然后进行归一化 utils.utility.standardizer
   3. 然后进行计算分数 average maximization aom moa等



# 保存

```py
from joblib import dump, load

# save the model
dump(clf, 'clf.joblib')
# load the model
clf = load('clf.joblib')
```

# Fast Train with SUOD

```python
from pyod.models.suod import SUOD

# initialized a group of outlier detectors for acceleration
detector_list = [LOF(n_neighbors=15), LOF(n_neighbors=20),
                 LOF(n_neighbors=25), LOF(n_neighbors=35),
                 COPOD(), IForest(n_estimators=100),
                 IForest(n_estimators=200)]

# decide the number of parallel process, and the combination method
# then clf can be used as any outlier detection model
clf = SUOD(base_estimators=detector_list, n_jobs=2, combination='average', verbose=False)
```
