---
title: "UniappStudy"
date: 2021-08-30T16:45:21+08:00
tags : [
   "wechat开发"
]
categories : [
   "学习"
]
series : []
aliases : []
draft: true
---

## 学习路径

先学vue。学完后学uni-app

看完[白话uni-app](http://ask.dcloud.net.cn/article/35657) 
看教程 vue


## 快捷键

ctrl + r 运行


## 小问题记录

1. 文件默认编译到Unpackage下
   1. 微信在unpackage/dev/mp-weixin即为编译后的项目地址。


# 学习uni-app和其他的不同

1. \<template>是一级节点  \<script> \<style>是并列的一级节点。

格式：
```html
<template>
    <view>
    </view>
</template>
<script>
</script>
<style>
</style>
```

2. 外部文件引用
```html
<script>  
    var util = require('../../../common/util.js');  //require这个js模块  
    var formatedPlayTime = util.formatTime(playTime); //调用js模块的方法  
</script>

<!--在util.js里，将function封装为方法 -->
<script>
function formatTime(time) {  
    return time;//这里没写逻辑  
}  
module.exports = {  
    formatTime: formatTime  
}
</script>
```

