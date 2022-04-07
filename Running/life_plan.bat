echo off
rem 自动化提交脚本
echo "build research block..."
rem build project.
set year=%date:~0,4%
set month=%date:~5,2%
set week=%date:~8,2%
set weekname=^" week plan"
rem set diarlyName=%diarlyName:/=-%


hugo new post/growthnotes/lifeplan/%1.md --kind lifeplan
echo "week plan block %1%.md build!"
echo week plan build. Have a nice day!
