Dim WShell
Set WShell = CreateObject("WScript.Shell")
WShell.Run "python D:\\PATH_TO_MAIN.py", 0
Set WShell = Nothing 