echo off
rem 创建月计划
echo "build research block..."
rem build project.
set year=%date:~0,4%
set month=%date:~5,2%
set monthname=^"%month:/=-% month plan"
rem set diarlyName=%diarlyName:/=-%


hugo new post/growthnotes/monthplan/%year%/%year%-%monthname%.md --kind monthplan
echo "month plan block %month% build!"
echo Month plan build. Have a nice day!
