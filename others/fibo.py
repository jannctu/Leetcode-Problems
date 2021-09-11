
# fibo = 1 1 2 3 5 8 13 21 

def my_fib(n): 
    fib_arr = [1,1]
    for i in range(2,n):
        fib_arr.append(fib_arr[i-1]+fib_arr[i-2])
    return fib_arr

def get_fibo(n): 
    fib_arr = [1,1]
    for i in range(2,n):
        fib_arr.append(fib_arr[i-1]+fib_arr[i-2])
    return fib_arr[-1]

print(my_fib(10))
print(get_fibo(10))