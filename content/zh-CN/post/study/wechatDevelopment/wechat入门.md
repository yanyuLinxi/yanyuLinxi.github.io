---
title: "Wechat入门"
date: 2021-08-27T15:26:05+08:00
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

# 文件类型

wxml => html
wxss => xss
.js => js
.json => json 配置文件。

# 配值文件
app.json 是当前小程序的全局配置，包括了小程序的所有页面路径、界面表现、网络超时时间、底部 tab 等；。 配置：https://developers.weixin.qq.com/miniprogram/dev/framework/config.html

## app.json:
    "pages":[所有页面] 第一个页面就是首页。
    小程序启动之后，在 app.js 定义的 App 实例的 onLaunch 回调会被执行:

project.config.json   程序开发者工具在每个项目的根目录都会生成一个 project.config.json，你在工具上做的任何配置都会写入到这个文件，当你重新安装工具或者换电脑工作时，你只要载入同一个项目的代码包，开发者工具就自动会帮你恢复到当时你开发项目时的个性化配置，其中会包括编辑器的颜色、代码上传时自动压缩等等一系列选项

page.json 其实用来表示 pages/logs 目录下的 logs.json 这类和小程序页面相关的配置。每个js都可以有page.json来配套配值 配值 https://developers.weixin.qq.com/miniprogram/dev/framework/config.html#%E9%A1%B5%E9%9D%A2%E9%85%8D%E7%BD%AE


# WXML

更换了html的标签。换为了view button text等等。


# WXSS

app.wxss  是全局样式
page.wxss 仅对当前页面生效

# JS学习：
1. js大概内容

```javascript
Page({
  data: { // 参与页面渲染的数据
    logs: []
  },
  onLoad: function () {
    // 页面渲染后 执行
  }
})
```

# 小程序API

有一些小程序官方的api   https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html


# 学习心得：
1. 大概弄明白了点东西：
   1. 对每一个page，有同名的js.wxml,wxss文件。分别控制逻辑，显示，样式
   2. 再js文件中，Page({})是当前页面。
      1. Page({data:{}, Event({})})  data是全局共享的数据。Event是当前页面的事件。
      2. 在wxml钟，通过bindtap将插件和事件进行绑定。