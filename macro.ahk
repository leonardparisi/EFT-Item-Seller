#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

dir    := A_ScriptDir
script  = %dir%\main.py
venv = %dir%\env\Scripts\python

^t::
MouseGetPos, xpos, ypos 
MsgBox, The cursor is at X%xpos% Y%ypos%.
return

^d::
Run, %ComSpec% /k %venv% "%script%",, Hide
return