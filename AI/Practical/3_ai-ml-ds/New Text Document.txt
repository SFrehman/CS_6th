@echo off
setlocal enabledelayedexpansion
title File Launcher

:start
cls
echo ==========================================
echo  FILES IN CURRENT DIRECTORY:
echo ==========================================
echo.

:: List files with numbers
set count=0
for /f "tokens=*" %%F in ('dir /b /a-d 2^>nul') do (
    if not "%%F"=="run.bat" (
        set /a count+=1
        set "file_!count!=%%F"
        echo [!count!] %%F
    )
)

if %count% equ 0 (
    echo No files found in this folder.
    pause
    exit /b
)

echo.
set /p choice="Select a file number to run (or Q to quit): "

if /i "%choice%"=="Q" exit /b

:: Validate input is a valid number in range
if not defined file_%choice% (
    echo.
    echo [ERROR] Invalid selection! Please enter a number between 1 and %count%.
    timeout /t 2 >nul
    goto start
)

:: Run the selected file using its default system program
echo.
echo Launching !file_%choice%!...
start "" "!file_%choice%!"
timeout /t 2 >nul
