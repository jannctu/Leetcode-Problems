# Length of Last Word

Given a string `s` consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return `0`.

A **word** is a maximal substring consisting of non-space characters only.

**Example 1:**
```python
Input: s = "Hello World"
Output: 5
```
**Example 2:**
```python
Input: s = " "
Output: 0
```

**Constraints:**
```python
* 1 <= s.length <= 10<sup>4</sup>
* s consists of only English letters and spaces ' '.
```

## My Solution 
I just used standard solution 
1. Trim the string. 
2. Split the string by `" "`.
3. Take the last word.
4. return length the last word. 

Thanks to `Python`, it can be done in just 1 line 😊
```python
def lengthOfLastWord(s):
        return len(s.strip().split(' ')[-1])
```

## My Submission 
![my-submissoin](my_submission.png)

