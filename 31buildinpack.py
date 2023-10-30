from statistics import mean
from math import pi
from time import time,ctime
print("enter the value of pi is ",pi)
seconds = time()
print("seconds since epoch(the point where time begins)=",seconds)
li=[1,2,3,3,2,2,2]
print("the averages of list values is:",end=" ")
print(mean(li))
local_time = ctime(seconds)
print("local time:",local_time)


