---
title: "常用其他python库"
date: 2021-09-30T08:41:46+08:00
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

# 常用库
1. yellowbrick 用来可视化画图的。
2. seaborn高端matplotlib画图的。
3. prettyplotlib  配合seaborn来画漂亮的图。
4. plotly Express 可视化。
5. tqdm进度条。
6. linux后台运行
   1. https://www.cnblogs.com/kaituorensheng/p/3980334.html

# 机器学习库
1. pyOD 用来做异常检测的。
2. plotly 可视化eda神器。
   1. 学习地址https://github.com/datawhalechina/wow-plotly
   2. 


# pip 更新注意
pip install selectivesearch -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
啊我吐了，一直retrying还有可能事因为pip版本太高。
python -m pip install pip==20.2 -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
通过该命令降级。
pip 安装报错试试这个。



# python 语法记录

1. params = dict(aa=bb, cc=dd) 来记录参数。