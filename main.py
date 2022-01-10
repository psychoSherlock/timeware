from time import time, sleep
from psutil import boot_time
from pyautogui import alert, password
import os
import ctypes
import hashlib


currentPath = os.path.dirname(__file__)


def uptime():
    return int(time() - boot_time()) // 60 # Convert seconds to minutes


try:
    with open(f'{currentPath}/dump.file', 'r') as f:
        activated = f.read()
except:
    activated = 'False'
    pass

wallpapper = f"{currentPath}/ad.jpg"

def countermeasures():
    sleep(300)
    alert(title="Overheat countermeasures warning!", text="Please shutdown your system or counter measures will be engaged in T-Minus 5 minutes!")
    sleep(300)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpapper , 0)
    os.system(f'{currentPath}\kill_tasks.vbs')
    alert(title="Counter measures engaged!", text="Countermeasures has been activated!" )
    sleep(30)
    os.system('shutdown /p')

print('Started')
def reactivate():
    os.system(f'{currentPath}\kill_tasks.vbs')
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpapper , 0)
    while True:
        user_pass = password(title="Password required!", text="Please unlock the system with password to continue using", mask="*")
        
        if user_pass:
            user_pass = hashlib.md5(user_pass.encode()).hexdigest()
        else:
            continue

        if user_pass=="f50a7083305cfdbbf01139ea8635e3ee": # Default password is timeware, md5 encode new password and replace it here
        
            alert('Success, device is now unlocked!')
            with open(f'{currentPath}/dump.file', 'w') as f:
                f.write('False')
            # ctypes.windll.user32.SystemParametersInfoW(20, 0, "PATH" , 0) Replace path with path to orginal wallpapper
            os.system('taskkill /F /IM cmd.exe /T')
            break
        else:
            alert('Access Denied!!')


while True:
    if uptime() >=240: # 4 hours in minutes
        alert(title="CPU overheated!",text="CPU has been running for more than 4 hours which is very bad for its health. To protect itself from crashing, please shutdown your system in T-Minus 10 minutes, or counter measures will be engaged!")
        break
    elif activated=="True":
        break
    
    sleep(300) # 5 minutes in seconds
    

with open(f'{currentPath}/dump.file', 'w') as f:
    f.write('True')

if activated=="True":
    print('reactivating..')
    reactivate()
elif activated=="False":
    print('Counter measures engaged')
    countermeasures()
