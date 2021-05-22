# Palindrome Number 
Given an integer `x`, return true if `x` is palindrome integer.

An integer is a **palindrome** when it reads the same backward as forward. For example, `121` is palindrome while `123` is not.

**Example 1:** 
```python
Input: x = 121
Output: true
```

**Example 2:** 
```python
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

**Example 3:** 
```python
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

**Example 4:** 
```python
Input: x = -101
Output: false
```

**Constraints:**
* -2<sup>31</sup> <= x <= 2<sup>31</sup> -1

 ## My Solutions 
There are 2 approaches to solve this problem
1. Mathematical (scientific) way
2. Street Fighter way 😝

But, both are lies on the same way to check wheater a number is palindrom or not, which is **reverse** the number, then compare with the original one. 
If the `reverse number` is same as the `original number` then it is a palindrome. there is one exception, which is the negative number always non palindrome. 

### Mathematical
The idea is using `Div` and `Mod` to extract each number and reverse them. 

```python
def isPalindromex(x):
    if x<0:
        return False 
    
    copy, reverse = x,0
    
    while copy: 
        reverse *= 10
        reverse += copy % 10
        copy //= 10
        
    return x == reverse
```

### Street Fighter 
This is simillar to the problem 7 (about reverse number). But, we need to handle the negative number. 
```python
def reverse(x):
    neg = False
    if x < 0: # check negative
        neg = True
        x = abs(x) #convert into positive 

    str_x=str(x) # convert int to string
    r_str_x=str_x[::-1] # reverse the string
    int_x = int(r_str_x) # convert back to int

    if neg: # if it is negative number
        int_x = int_x * -1

    return int_x

def isPalindrome(x: int):
    if x < 0:
        return False

    if x == reverse(x): 
        return True 
    return False
```

## My Submission
This screenshoot is for the `Street Fighter` Solution
![my-submission](my_submission.png)


