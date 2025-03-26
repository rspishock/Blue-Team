@echo off


rem *********************************************
rem *        Environmental preperation          *
rem *********************************************
set directory=c:\Security__Test_%date:~4,4%-%date:~10,2%-%date:~7,2%_%time:~0,2%%time:~3,2%_%time:~6,5%
if exist '%directory%' (
    echo y | rd /s '%directory%'
)
md '%directory%'
cd '%directory%'
goto End
:End

rem *********************************************
rem *               Perform scan                *
rem *********************************************
rem view network shares
net share \\127.0.0.1 >> netshares.txt

rem view network sessions
net session

