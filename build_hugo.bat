echo off
rem 自动化提交脚本
echo "Deploying updates to GitHub..."
rem build project.

hugo -d docs -t pure

git add docs
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
