:menu
cls
@echo off
echo ############################################
echo ##                                        ##
echo ##      Automation QA from Azure          ##
echo ##                                        ##
echo ## Version: 2.8.20                        ##
echo ############################################
echo.
echo 1 - Generate the manual evidence.
echo 2 - Run the automation.
echo 0 - Exit
echo.
set /p Comando= Choose the option:

if "%Comando%" equ "1" (goto:op1)
if "%Comando%" equ "2" (goto:op2) 
if "%Comando%" equ "0" (goto:exit)
if not "%Comando%" equ "0" if not "%Comando%" equ "1" if not "%Comando%" equ "2" (goto:wrong_option)

:op1
cd ..\..
python generateManualEvidence.py
pause
exit

:op2
cd ..\..
python automatizationCore_Azure.py
pause
exit

:wrong_option
echo Wrong option. Please try again.
pause
goto:menu

