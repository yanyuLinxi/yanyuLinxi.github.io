echo off
rem 自动化提交脚本
echo "build research block..."
rem build project.

hugo new post/paperreading/%1%.md --kind paperreading
echo "research block post/paperreading/%1%.md build!"
