import sys
import subprocess
import time
from decouple import config # python-decouple
import datetime
import webbrowser

def is_time_between(begin_time, end_time, check_time=None):
    check_time = check_time or datetime.datetime.now().time()
    print(check_time)
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else: # crosses midnight
        return check_time >= begin_time or check_time <= end_time

def welcome():
    if is_time_between(datetime.time(6,30), datetime.time(14,30)):
        webbrowser.open('https://www.youtube.com/watch?v=zofBinqC2F4', new=2)
    elif is_time_between(datetime.time(14,30), datetime.time(20,30)):
        subprocess.call([r'C:\GENERAL\Games\Diablo II\Diablo II.exe'])
    else:
        subprocess.Popen(['python', 'blink.py'], stdout=subprocess.PIPE)

IP_DEVICE = config('IP_DEVICE')

success_str = 'Reply from ' + IP_DEVICE + ': bytes='
is_not_home = True

while is_not_home:
    proc = subprocess.Popen(['ping', IP_DEVICE], stdout=subprocess.PIPE)

    while is_not_home:
        line = proc.stdout.readline().decode('utf-8')
        if not line:
            break

        print(line)
        if success_str in line:
            welcome()
            is_not_home = False
            break
        else:
            print('Fail')
    
    time.sleep(30)
