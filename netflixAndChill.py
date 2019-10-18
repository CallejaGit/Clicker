import pyautogui 
import subprocess
import time
import os

output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
x_axis, y_axis = "", ""

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

num = int(input("Enter Unix Epoch: "))

# poor man's scheduler
tick = 0;
while time.time() < num:
    # do nothing
    os.system('clear')

    wait(tick)
    tick = (tick + 1) % 500
pyautogui.click(x_axis, y_axis)
print time.time()

def representsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def wait(tick):
    if tick == 0:
        print("waiting")
    elif tick == 100:
        print("waiting.")
    elif tick == 200:
        print("waiting..")
    elif tick == 300:
        print("waiting...")


