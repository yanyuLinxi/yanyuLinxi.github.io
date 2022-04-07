echo off
rem 创建diary
echo "build research block..."
rem build project.
set year=%date:~0,4%
set month=%date:~5,2%
set diarlyName=^"%date:/=-% Diary"
rem set diarlyName=%diarlyName:/=-%


hugo new post/growthnotes/diary/%year%/%month%/%diarlyName%.md --kind dailydiary
echo "Daily diary block %diarlyName% build!"
echo Have a nice day!
