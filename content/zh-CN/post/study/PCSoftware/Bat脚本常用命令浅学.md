---
title: "Bat脚本常用命令浅学"
date: 2022-04-07T10:24:25+08:00
tags : [

]
categories : [
    "学习"
]
series : []
aliases : []
draft: false
toc: true
math: true
---

## 基础语法
1. 赋值的时候等号两边没有空格
   1. set a=%b
2. 取值：%a
3. 输出变量：%a%

## 常用命令
1. @REM 注释

2. xcopy 批量复制文件夹
   1. 实例： xcopy /e/y/i/f source destination
   2. 参数解释：
      1. /e 复制所有子目录，即使它们是空的。将/e与/s和/t命令行选项一起使用。
      2. /y 禁止提示确认您要覆盖现有目标文件。
      3. /i 如果Source是目录或包含通配符且Destination不存在，则xcopy假定Destination指定目录名称并创建新目录。然后，xcopy将所有指定的文件复制到新目录中。默认情况下，xcopy会提示您指定Destination是文件还是目录。
      4. /f 复制时显示源文件名和目标文件名。
      5. /? 提供帮助
3. %cd% 获取当前路径。
4. 判断参数为空


```bat
@REM 空格都不能写错
if "%one%"=="" (
     set msg="rebuilding site %date% %time%"
 )else (
     set msg="%one% rebuilding site %date% %time%"
 )
```