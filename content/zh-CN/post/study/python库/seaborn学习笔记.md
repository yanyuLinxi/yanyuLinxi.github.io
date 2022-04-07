---
title: "Seaborn学习笔记"
date: 2021-09-30T08:51:28+08:00
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
seaborn结合pandas来画好看的图。

最后网页显示的统计图，可以用seaborn画。

# 基本使用

1. seaborn中两种函数，第一种返回当前设置，第二种设置
## 管理图表样式

axes_style, set_style 返回样式、设置样式

### 主题
#### darkgrid

白线灰底。不影响数据表示

#### whitegrid

白底，简洁大方，数据元素较大使用。

#### dark

没有格子的灰底

#### white

没有格子的白底

#### ticks

给轴线分割线段

### 布局

使用plotting_context()返回布局。set_context来设置布局。

布局按相对大小排序分别是：paper, notebook, talk,和poster  

影响标题、线型等。默认时notebook。

临时设置布局
with sns.plotting_context()

### 配色方案

1. 使用color_palette()和set_palette()建立配色方案

color_palette()可以接受的颜色参数形式
+ HTML十六进制字符串（hex color codes）
    + color = '#eeefff'       

+ 合法的HTML颜色名字（HTML color names）
    + color = 'red'/'chartreuse'      

+ 归一化到[0, 1]的RGB元组（RGB tuples）
    + color = (0.3, 0.3, 0.4)

2. 色环
   1. 共用API：
      1. sns.palplot(色环) 显示色环
      2. sns.color_palette(色环) 获取色环
      3. sns.set_palette(色环) 设置色环， 和color_palette同参数
      4. 每个色环有自己的专门设置的函数，比如hsl: sns.hsl_palette()
   2. Qualitative color palettes  **当需要区分离散的数据集，且数据集之间没有内在的顺序**
      1. 使用色环代码：
         1. sns.color_palette("hls", 10)  **hls最为常用**, husl 在亮度和饱和度上更平均
            1. 第一个参数是色环，第二个参数是颜色个数。 
            2. l 亮度
            3. s 饱和度。
         2. 或者使用sns.huso_palette()函数来调用，两个函数类似。
            1. 参数 start 开始
            2. rot number of rotations
            3. as_cmap=True 返回colormap对象。
            4. dark, light 控制亮度。
      2. sns.hls_palette(8, l=.3, s=.8) # l是亮度（lightness），s是饱和度（saturation） 使用hls循环配色 最为常用。
   3. Color Brewer颜色循环。 在某些情况下颜色会循环重复 某些颜色循环系统对色盲比较友好（尤其是红绿色盲）
      1. Paired
      2. Set2 
   4. sequential color palettes **当数据集的范围从相对低值（不感兴趣）到相对高值（很感兴趣）**
      1. "Blues"
      2. "BuGn_r" 添加r倒置，逆序。绿色。
      3. "GnBu_d" 添加后缀d，则颜色加深
      4. "cubehelix" 颜色线性变化，打印后也能区分不同颜色，对色盲友好。
         1. cubehelix专属函数: sns.cubehelix_palette可以进一步设置这个色环的更多参数
            1. 可以通过dark, light控制亮度、暗度。
            2. 通过reverse参数控制是否reverse
      5. sns.light_palette("green") 从明亮向暗产生渐变。 返回可以通过set_palette()设置的颜色
      6. sns.dark_palette("purple")从暗向明产生渐变
   5. Diverging color palettes。**当数据集的低值和高值都很重要，且数据集中有明确定义的中点时**
      1. BrBG  两端的颜色应该具有相似的亮度和饱和度，中间点的颜色不应该喧宾夺主
      2. coolwarm  常用的diverging 调色
         1. center="dark" 将中间设置为黑色。
         2. sep参数controls the width of the separation between the two ramps in the middle region of the palette
      3. diverging_palette 函数使用'husl'颜色系统，需要在函数中设置两个hue参数，也可以选择设置两端颜色的亮度和饱和度
   6. color_palette()与set_palette()的关系，类似于axes_style()和set_style()的关系  set_palette()的参数与color_palette()相同。 区别在于，set_palette()会改变配色方案的默认设置，从而应用于之后所有的图表。总之就这两个函数来选择配色方案。
   7. 临时设置配色方案: with sns.color_palette("PuBuGn_d"):
3. sns.choose_colorbrewer_palette()能够以互动的方式测试、修改不同的参数
   只能用于Jupyter Notebook

# 绘图

# 绘制单变量分布图

1. sns.displot()绘制分布图
   1. 旧版：kind="hist"直方图 kind="kde"核密度图， kind="ecdf"
   2. 新版： hist=True设置为直方图。
   3. rug=True为每个观察值添加一个tick
   4. kde=True 打印核密度
2.  sns.histplot()函数，绘制直方图，
3.  sns.kdeplot()
    1. 相对于sns.distplot()能够设置更多选项
    2. 设置shade参数，填充核密度线下方区域
    3. bw_method 确定要使用的平滑带宽的方法
    4. bw_adjust 参数和bin很像。乘法缩放使用 选择的值的因子
    5. cut 正如您在上面看到的，高斯 KDE 过程的性质意味着估计超出了数据集中的最大值和最小值。可以使用 ``cut`` 参数控制绘制曲线超过极值的距离。但是，这仅影响曲线的绘制方式，而不影响曲线的拟合方式。
    6. ax参数选择图表绘制在哪个坐标系内
    7. n_levels=60 通过n_levels参数，增加轮廓线的数量，达到连续化核密度图的效果
4. rugplot() 绘制出现点

## notes:
1. label 

# 绘制双变量分布图
1. sns.jointplot
   1. 散点图  默认绘制散点图
      1. (x="x", y="y", data=df)
      2. 注意Seaborn与DataFrame联合使用，data参数指定DataFrame，x、y参数指定列名
   2. 六边形图（hexbin plot）
      1. 六边形颜色的深浅，代表落入该六边形区域内观测点的数量，常应用于大数据集，与white主题结合使用效果最好
      2. sns.jointplot(x=x, y=y, kind="hex", color="k") # kind参数设置六边形图
   3. 核密度图（kernel density estimation）
      1. kind="kde"
   4. 而sns.jointplot()只能单独绘制，无法添加在其他图表之上
   5. sns.jointplot()绘制后返回JointGrid对象对象，可以通过JointGrid对象来修改图表，例如添加图层或修改其他效果
      1. g = sns.jointplot
      2. g.plot_joint(plt.scatter, c="w", s=30, linewidth=1, marker="+")
      3. 

# 其他画图api
1. FacetGrid
   1. 一次花多个图。

# 可视化数据集的成对关系

1. sns.pairplot()
2. PairGrid对象
   1. g = sns.PairGrid(iris)
# API

1. despine()移除右侧上方的横线
   1. 默认上右。传入left等参数控制哪边被移除
2. 临时设置主题：with sns.axes_style()




# seaborn 图
1. 散点图 scatterplot
   1. hue设置不同点的标签。