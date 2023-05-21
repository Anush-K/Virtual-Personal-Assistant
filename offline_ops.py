import os
import subprocess as sbp
from datetime import datetime

paths = {
    'notepad': "C:\Windows\\notepad.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

def camera():
    sbp.run('start microsoft.windows.camera:', shell=True)

def notepad():
    os.startfile(paths['notepad'])

def calculator():
    sbp.Popen(paths['calculator'])  

def cmd():
    os.system('start cmd')

def say_time():
    now = datetime.now()
    current_time = now.strftime("%H   %M")
    return current_time