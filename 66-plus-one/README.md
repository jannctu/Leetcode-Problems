# Plus One

Given a **non-empty** array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

**Example 1:**
```
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
```

**Example 2:**
```
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
```

**Example 3:**
```
Input: digits = [0]
Output: [1]
```

**Constraints:**

* `1 <= digits.length <= 100`
* `0 <= digits[i] <= 9`

## My Solution 
```python
class Solution:
    
    def Convert(self,string):
        list1=[]
        list1[:0]=string
        return list1

    def plusOne(self, digits: List[int]) -> List[int]:
        str_num = ''
        for i in range(len(digits)): 
            str_num += str(digits[i]) 
        
        int_num = int(str_num) + 1
        return self.Convert(str(int_num))
```

## My Submission 

