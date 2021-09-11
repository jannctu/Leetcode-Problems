# 258. Add Digits

Given an integer `num`, repeatedly add all its digits until the result has only one digit, and return it.

**Example 1:**
```
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
```

**Example 2:**
```
Input: num = 0
Output: 0
``` 

**Constraints:**

* `0 <= num <= 231 - 1`
 

**Follow up:** Could you do it without any loop/recursion in O(1) runtime?


## My solution

```python
class Solution:
    def addDigits(self, num: int) -> int:
        ans = num
        while(len(str(num)) > 1): 
            new_num = 0
            for i in range(len(str(num))):
                new_num += int(str(num)[i])
            num = new_num
        ans = num
        return ans
```

## My Submission
