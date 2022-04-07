echo off
rem 生成内容复制到文件夹，然后同步网站内容到github
echo "Deploying updates to GitHub..."
rem build project.

set cur_path=%cd%
set destination=%1
if "%destination%"=="" ( 
    set destination=%cur_path%/../yanyuLinxi.github.io
)
echo cur path: "%cur_path%"
echo destination dir: "%destination%"

@REM 定义需要复制的文件夹
set project=study essay journey paperreading 
for %%p in (%project%) do (
    @REM 循环复制文件夹到指定目录
    xcopy "%cur_path%/content/zh-CN/post/%%p" "%destination%/content/zh-CN/post/%%p" /e/y/i/f
)


@REM 生成内容文件并同步到github上
cd %destination%
echo %cd%


hugo -d docs -t hugo-theme-next

git add docs
rem commit changes
rem get params
set comment=%2
if "%comment%"=="" (
    set msg="rebuilding site %date% %time%"
)else (
    set msg="%comment% rebuilding site %date% %time%"
)
echo commit is %msg%

git commit -m %msg%
git push origin master