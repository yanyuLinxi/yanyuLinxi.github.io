---
title: "Matplotlib-2学习"
date: 2021-09-29T10:20:26+08:00
tags : [
   "python相关库学习",
   "机器学习相关库",
   "matplotlib", 
]
categories : [
   "学习"
]
series : []
aliases : []
draft: false
---

# 概览

# setting

## 不同风格
1. 
plt.style.available 打印样式列表
plt.style.use('seaborn') 使用seaborn风格的图。

2.
参数color可选项：
b:blue  c:cyan  g:green k:black
m:magenta r:red w:white y:yellow

3.
结束时
plt.legend() 在图上放置图例。

## 设置坐标轴
plt.xlim(-1, 3.5) #设置x坐标在-1到3.5

plt.xlabel('degree'); plt.ylabel('rms error')
设置横纵坐标的名称。

# 图

## scatter

plt.scatter(x, y, s=None float array, c array-like color map, marker, cmap)

c是一组数，标注了每个点根据标签使用不同的色彩。

s是 marker size in points**2 就是粗细
cmap 就是色彩图。
optional: rainbow; Blues; spring

## 线图
plt.plot

1. plot可以接收多个x,y参数，只要依次给过去就行。在show前绘制的所有plot都能画在一张图上。

## 柱状图

plt.bar

## 热力图

plt.heat

## 其他图

plt.box箱图
plt.hist 直方图
plt.pie 饼图
plt.area 面积图

## imshow

## subplots

1. 
fig, ax = plt.subplts(row, columns, figsize=(subplots figsize))

row是只子图占用父图多宽。
ax[i]就是子图对象，在上面画图
ax[i].scatter(x[:, 0], x[:, 1])等

2. 
plt.figure(figsize=(row, columns))
ax = fig.add_subplot(row, column, idx )
**idx 从1开始增加。**
ax 画图 如 ax.plot

3. 参数
   1. nrows, subplot行
   2. ncols 列
   3. sharex sharey subplot中x、y共享。同时影响所有plot

## 图的其他信息

1. plt.legend(loc) 画图例。在图上哪个地方画图例。
   1. 画线时标记label就会显示legand。或者legend有方法后添加图例
   2. label = _nolegend_ 就不会显示图例
   3. loc=0就是自动选择best位置来显示。
   4. ncol=2  控制legand有几列。
2. plt.grid(True) 显示图片背景中的格子
   1. plt.grid(b=True, which='major', axis='both')
   2. which指定绘制的网格刻度类型（major、minor或者both）
   3. axis指定绘制哪组网格线（both、x或者y）
3. 设置横纵轴
   1. plt.axis() # shows the current axis limits values；如果axis方法没有任何参数，则返回当前坐标轴的上下限
   2. (1.0, 4.0, 0.0, 12.0)
   3. plt.axis([0, 5, -1, 13]) # set new axes limits；axis方法中有参数，设置坐标轴的上下限；参数顺序为[xmin, xmax, ymin, ymax]
   4. 同样的方法可以用xlim, ylim来设置。
4. 设置标题
   1. plt.title('Simple plot')
5. 保存图片
   1. plt.savefig('plot123_2.png', figsize=[8.0, 6.0], dpi=200)
6. 设置样式
   1. 设置颜色
      1. plt.plot(x, y, "color value")
      2. 可以为16进制字符串，可以为灰度值，可以为rgb三元组，可以为别名

|  颜色  | 别名  | HTML颜色名 | 颜色  | 别名  | HTML颜色名 |
| :----: | :---: | :--------: | :---: | :---: | :--------: |
|  蓝色  |   b   |    blue    | 绿色  |   g   |   green    |
|  红色  |   r   |    red     | 黄色  |   y   |   yellow   |
|  青色  |   c   |    cyan    | 黑色  |   k   |   black    |
| 洋红色 |   m   |  magenta   | 白色  |   w   |   white    |

   2. alpha 设置透明度
   3. 参数:ls 设置线形。 "-"实线， ':'虚线, '--'破折线 'steps'阶梯线, '-.'点划线 'None'什么都不画。表示实线
   4. lw 表示线宽。
   5. marker 设置标志。用来标志数据的位置。
| 标记  |       描述       |        标记        |       描述       |
| :---: | :--------------: | :----------------: | :--------------: |
|  '1'  | 一角朝下的三脚架 |        '3'         | 一角朝左的三脚架 |
|  '2'  | 一角朝上的三脚架 |        '4'         | 一角朝右的三脚架 |
|  'v'  | 一角朝下的三角形 |        '<'         | 一角朝左的三角形 |
|  '^'  | 一角朝上的三角形 |        '>'         | 一角朝右的三角形 |
|  's'  |      正方形      |        'p'         |      五边形      |
|  'h'  |     六边形1      |        'H'         |     六边形2      |
|  '8'  |      八边形      |
|  '.'  |        点        |        'x'         |        X         |
| '\*'  |       星号       |        '+'         |       加号       |
|  ','  |       像素       |
|  'o'  |       圆圈       |        'D'         |       菱形       |
|  'd'  |      小菱形      | '','None',' ',None |        无        |
| '\_'  |      水平线      |         '          |        '         | 竖线 |

更多的plot设置:
|      参数       |     描述     |      参数       |     描述     |
| :-------------: | :----------: | :-------------: | :----------: |
|    color或c     |   线的颜色   |  linestyle或ls  |     线型     |
|  linewidth或lw  |     线宽     |     marker      |     点型     |
| markeredgecolor | 点边缘的颜色 | markeredgewidth | 点边缘的宽度 |
| markerfacecolor | 点内部的颜色 |   markersize    |   点的大小   |

1. 设置背景色
   1. 设置背景色，通过向plt.axes()或者plt.subplot()方法传入axisbg参数，来设置坐标轴的背景色
2. 坐标轴刻度：
   1. xticks()和yticks()方法。设置坐标轴的刻度。
3. 其他图
   1. 柱状图 bar
   2. 水平柱状图 barh
   3. 箱线图 boxplot
   4. 散点图 scatter
      1. s设置散点大小 c设置散点颜色。 marker设置散点形状
   5. 阶梯图 step
   6. 条形图 bar
   7. 条带图 fill_between
   8. 直方图 hist
      1. bins 分类数量
      2. normed 归一化处理
      3. orientation 水平或垂直图
      4. align 居中或者左右。
      5. cumulative 累计直方图
   9. 误差条 errorbar
   10. 饼图 pie
   11. 极坐标图 polar
   12. 网格线 rgrids() thetagrids()
4. 图形中的文字放置：
    1. plt.text(0.1, -0.04, 'sin(0)=0'); # 位置参数是坐标
    2. plt.annotate()在途中加注释
    3. annotate()绘制箭头
5. matplotlib对象分为三层：
    1. FigureCanvas。直接使用pyplot as plt绘制的。
    2. fig = plt.figure() 使用图像绘制的
    3. Axes axes = fig.add_axe()
    4. 从属关系，plt最大，axes最小。都从上一级调用
    5. 使用axes和fig.add_subplot()的区别。subplot不能控制具体的位置。无法设置嵌套的结构。
6. twinx() twiny() 从其他数据那里复制x坐标和y坐标。
7. sharex sharey 共享x、y坐标轴
8. 设置对数坐标轴 set_yscale, semilogx loglog etc.
9. 设置中央坐标轴
   1. ax.spines
   2. ax.set_position
10. 设置等高线: pcolor
11. contour() contourf() 地形图
12. 3D 图
13. 曲面图
    1.  映射等高线
## API

1. plt.fill_between
   1. x, x+i, x-i, facecolor="基础色", alpha：透明度