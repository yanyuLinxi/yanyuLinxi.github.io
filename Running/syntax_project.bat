echo off
rem 创建doc文件并push到远程
echo "Deploying updates to GitHub..."
rem build project.

git add .
rem commit changes
rem get params
set one=%1
if "%one%"=="" (
    set msg="rebuilding site %date% %time%"
)else (
    set msg="%one% rebuilding site %date% %time%"
)
echo commit is %msg%

git commit -m %msg%
git push origin master
