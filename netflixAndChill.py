import pyautogui 
import subprocess
import time
import os
from datetime import date
from datetime import datetime


# poor man's loading UI
def waiting(tick):
    if tick == 0:
        os.system('clear')
        print("waiting")
    elif tick == 1000000:
        os.system('clear')
        print("waiting.")
    elif tick == 2000000:
        os.system('clear')
        print("waiting..")
    elif tick == 3000000:
        os.system('clear')
        print("waiting...")

# makesure it will click on the centre of the screen
output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
x_axis, y_axis = "", ""


# Prompts user when the event occurs
user_input_hh = raw_input("Enter hour in 24h format ##: ")
user_input_mm = raw_input("Enter minutes in 24h format ##: ")
user_input_ss = raw_input("Enter seconds 24h format ##: ")

# Set up to conver EST > Unix Epoch
set_time = date.today().strftime("%d/%m/%Y") + " " + user_input_hh + \
        ":" + user_input_mm + ":" + user_input_ss
unix_epoch = time.mktime(datetime.strptime(set_time, "%d/%m/%Y %H:%M:%S").timetuple())

# poor man's regex
by = False;
for s in output:
    
    if s == '\n':
        break
    elif s == 'x':
        by = True
    else:
        if not by:
            x_axis += s
        else:
            y_axis += s

x_axis = int(x_axis) / 2
y_axis = int(y_axis) / 2

# poor man's scheduler
tick = 0;
while time.time() < unix_epoch:
    waiting(tick)
    tick = (tick + 1) % 5000000
print("enjoy")
pyautogui.click(x_axis, y_axis)
