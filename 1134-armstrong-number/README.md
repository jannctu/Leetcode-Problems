# Armstrong Number

Given an integer `n`, return `true` if and only if it is an **Armstrong number**.

The `k`-digit number `n` is an **Armstrong number** if and only if the k<sup>th</sup> power of each digit sums to `n`.

 

**Example 1:**

Input: n = 153
Output: true
Explanation: 153 is a 3-digit number, and 153 = 13 + 53 + 33.
**Example 2:**

Input: n = 123
Output: false
Explanation: 123 is a 3-digit number, and 123 != 13 + 23 + 33 = 36.
 

**Constraints:**

* 1 <= `n` <= 10<sup>8</sup>

## My Solution
**Approach 1: Convert into Strings**
```python 
class Solution:
    def isArmstrong(self, n: int) -> bool:
        str_n = str(n)
        p = len(str_n)
        sq = 0 
        
        for i in str_n:
            sq += int(i)**p
        return sq == n
```

**Approach 2: Mathematical Way**
```python
import math
class Solution:
    def getTheSum(self,n,p):
        out = 0 
        while(n!=0):
            out += (n%10)**p
            n = n // 10
        return out
    
    def isArmstrong(self, n: int) -> bool:
        p = int(math.log10(n)) + 1
        return self.getTheSum(n,p) == n
```

## My Submission
![img.png](img.png)
![img_1.png](img_1.png)

