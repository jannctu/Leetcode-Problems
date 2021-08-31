import random
from datetime import datetime
data = []
for i in range(0,30):
    n = random.randint(1,10)
    data.append(n)

data.sort()
print(data)
def binary_search(x,data):
    start = 0
    end = len(data)
    while start < end: 
        mid = (start + end) // 2
        if x == data[mid]:
            return mid
        elif x > data[mid]:
            start = mid+1
        else:
            end = mid

    return -1 

start_time = datetime.now()
print(binary_search(12,data))
finish_time = datetime.now()
print(finish_time-start_time)