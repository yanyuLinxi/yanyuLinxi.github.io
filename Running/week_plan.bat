echo off
rem 自动化提交脚本
echo "build research block..."
rem build project.
set year=%date:~0,4%
set month=%date:~5,2%
set week=%date:~8,2%
set weekpre=^" week "
set weektail=" plan"
rem set diarlyName=%diarlyName:/=-%


hugo new post/growthnotes/weekplan/%year%/%month%/%year%-%month%%weekpre%%1%weektail%.md --kind weekplan
echo "week plan %month% build!"
echo week plan build post/growthnotes/weekplan/%year%/%month%/%year%-%month%%weekpre%%1%weektail%.md Have a nice day!
