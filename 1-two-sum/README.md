## Problem Definition
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have <b><i>exactly one solution</i></b>, and you may not use the same element twice.

You can return the answer in any order.

**Example 1:**
```
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Output: Because nums[0] + nums[1] == 9, we return [0, 1]. 
```

**Example 2:**
```
    Input: nums = [3,2,4], target = 6
    Output: [1,2] 
```

**Example 3:**
```
    Input: nums = [3,3], target = 6
    Output: [0,1] 
```


**Constraints:**

* `2 <= nums.length <= 10^4`
* `-10^9 <= nums[i] <= 10^9`
* `-10^9 <= target <= 10^9`
* <b>Only one valid answer exists.</b>

## Solutions 
### Solution 1: Brute Force 

Simple double for could be implemented to solve this problem 

<b>Python</b>
````python
def twoSum(nums: List[int], target: int):        
    for i in range(0,len(nums)-1): 
        for j in range(i+1,len(nums)):
            print(nums[i] + nums[j])
            if nums[i] + nums[j] == target: 
                return [i,j]
    return []
````

<b>Java</b>
````java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++)  {
                if (nums[i] + nums[j] == target) {
                    return new int[] {i, j};
                } 
            }
        }

        return new int[] {};
    }
}
````

### Solution 2: Dictionary
Take the complements and store in `Dictionary`

<b>Python</b>
```python
def twoSum(nums: List[int], target: int):        
     d = {}
    for i in range(0, len(nums)): 
        sisa = target - nums[i]
        
        if nums[i] in d.keys():
            return [i,d[nums[i]]]
        else:
            d[sisa] = i
```

<b>Java</b>
```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numDic= new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
           int sisa = target - nums[i];

           if (numDic.containsKey(sisa)) {
               return new int[] {i, numDic.get(sisa)};
           } else {
               numDic.put(nums[i], i);
           }
        }

        return new int[] {};
    }
}
```


## My submission 
Here is my submission on Leedcode.com 
![mysubmission-problem1](my_submission.png)