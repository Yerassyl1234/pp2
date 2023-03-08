import time
a = int(input())
wait = int(input())
time.sleep(wait/1000)
print(("Square root of {} after {} miliseconds is {}").format(a,wait,a**(1/2)))