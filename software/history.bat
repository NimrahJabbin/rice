@ECHO OFF
TASKKILL /F /IM "main.exe"
del main.exe
del noorehidayat.ttf
del /a "D:check.txt"
del /a "E:check.txt"
del /a "F:check.txt"
del /a "H:check.txt"
del /a "I:check.txt"
rmdir /s /q mpil
rmdir /s /q img
