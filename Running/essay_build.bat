echo off
rem 输入 %1是文件夹名 %2是文件名
echo "build path file block..."
rem build project.

rem 先输入path 是posts下的path 然后输入文件名
hugo new post/essay/%1/%2.md  --kind essay
echo "posts/essay/%1/%2.md build!"