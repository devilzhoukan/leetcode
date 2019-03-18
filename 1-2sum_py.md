
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].



n^2的算法就不说了，肯定上hash
想的是过一遍建立hashtable（enumerate和dict真方便），再过一遍找对的答案。
其间出现了问题，就是题目要求一个数不能用两次，但是又可能出现两个一样的数，想了会就用数组存下数的位置，如果出现多次就在数组里append

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDic = {}
        for i,value in enumerate(nums):
            if value not in numsDic:
                numsDic[value] = [i]
            else:
                numsDic[value].append(i)    
        for i in nums:
            minus = target - i
            if i == minus:
                if len(numsDic[i]) < 2:
                    continue
                else:
                    return numsDic[i][0:2]
            if minus in numsDic:
                return [numsDic[i][0], numsDic[minus][0]]
        return None
```

>Runtime: 40 ms, faster than 79.93% of Python3 online submissions for Two Sum.  
>Memory Usage: 15.7 MB, less than 5.08% of Python3 online submissions for Two Sum.

内存我就不管了，只管速度。看了下答案，one pass hash只过一遍，边存边找，而且好像还自然而然地解决了相同数的问题


```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDic = {}
        for i,value in enumerate(nums):
            minus = target - value
            if minus in numsDic:
                return [numsDic[minus], i]
            else:
                numsDic[value] = i
        return None
```
>Runtime: 40 ms, faster than 79.93% of Python3 online submissions for Two Sum.  
>Memory Usage: 14.3 MB, less than 5.83% of Python3 online submissions for Two Sum.

为啥，我感觉我这明显简短了很多，one pass不说，还省下了新建list的时间，为什么1ms都没减少？？？