#CREATE A TIME COUNTDOWN IN PYTHON
import time

seconds = 10
while seconds:
    mins,secs = divmod(seconds,10)
    timer = '{:02d}:{:02d}'.format(mins,secs)
    print(timer,end="\r")
    time.sleep(1)
    seconds -= 1

print("Time's up")
