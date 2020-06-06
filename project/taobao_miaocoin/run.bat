@echo off
%~d0
cd %~dp0
cd ADB
adb.exe devices
pause
