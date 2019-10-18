import pyautogui 
import subprocess
import time

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

# poor man scheduler
while time.time() < num:
    # do nothing
    print("waiting\n")
pyautogui.click(x_axis, y_axis);
print time.time()

def representsInt(s):
    try: 
        int(s)
        return True;
    except ValueError:
        return False


