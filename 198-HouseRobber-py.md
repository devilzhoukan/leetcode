## 198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:
```
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
```

I don't know whether it is a DP problem or not.
But obviously I use a "DP" array first then I notice that no array is needed.

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        p_max = 0
        pp_max = 0
        for index, value in enumerate(nums):
            temp = pp_max
            pp_max = p_max
            p_max = max(p_max, temp+value)
        return p_max
```

*Notice*: no 0 and 1 index check is needed here. 

I use p and pp to show previous(maxlist[i-1]) and pre-previous(maxlist[i-2])
