import pyautogui
import time

message = "I LOVE YOU 3000 ❤ "
n=3000

print("start")
count = 5
while(count !=0):
    time.sleep(1)
    count -= 1

print("\n complete")

for i in range (0, int(n)):
    pyautogui.typewrite(message + '\n')
