from math import sqrt

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <=2: 
            return 0 
        
        non_prime = {}
        for i in range(2,int(sqrt(n))+1): 
            if i not in non_prime: 
                for j in range(i*i,n,i):
                    non_prime[j] = 1
                
        return n - len(non_prime) - 2 


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True 

def count_prime(n): 
    nn = range(n)
    counter = 0 
    for i in range(n): 
        if is_prime(i):
            counter +=1 
    return counter

n=10
print(is_prime(n))
print(count_prime(n))

s = Solution()

print(s.countPrimes(10))