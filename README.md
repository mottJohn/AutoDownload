# AutoDownload

## What you need
1. [Freebyte Task Scheduler](http://www.freebyte.com/fbtaskscheduler/)
2. a .py file for downloading from website
3. a .bat file for running in Windows

## Setting up .bat file
The .bat file just looks like this. The first part is the path of where you [installed Python](https://github.com/mottJohn/Python_101). The second part is the path of the .py file.

C:\Users\CHA82870\AppData\Local\Continuum\anaconda3\python.exe "C:\Users\CHA82870\OneDrive - Mott MacDonald\Documents\autodownload-from-web\downloadWindDate_3RS.py %*"

To get the path of the installed Python, open anaconda prompt, and type where python.

## Setting up Freebyte Task Scheduler
1. Click the plus icon
2. Everything else is straight forward. Just remember to put the path of your .bat file in program location tab and leave program parameters tab blank.

## .py files
* downloadWindData_KaiTak.py (use together with run_WindDate_KaiTak.bat)
