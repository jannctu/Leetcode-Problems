import random
from datetime import datetime
data = []
for i in range(0,100):
    n = random.randint(1,10)
    data.append(n)

def most_frequent(d): 
    max_counter = 0 
    visited_num = {} 
    ans = None

    for i in d: 
        if i not in d: 
            d[i] = 1
        else:
            d[i] += 1 
        
        if d[i] > max_counter:
            max_counter = d[i]
            ans = i
            print(f"num:{ans} freq:{max_counter}")

    return ans


print(most_frequent(data))