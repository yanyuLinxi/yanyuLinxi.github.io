echo off
rem 自动化构建文件
echo "build path file block..."
rem build project.

rem 先输入path 是posts下的path 然后输入文件名
hugo new post/research/%1/%2.md --kind research
echo "post/research/%1/%2.md build!"