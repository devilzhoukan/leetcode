Given a list of positive integers nums and an int target, return indices of the two numbers such that they add up to a target - 30.

Conditions:

- You will pick exactly 2 numbers.
- You cannot pick the same element twice.
- If you have muliple pairs, select the pair with the largest number.

```
Input: nums = [1, 10, 25, 35, 60], target = 90
Output: [2, 3]
Explanation:
nums[2] + nums[3] = 25 + 35 = 60 = 90 - 30
```

```
Input: nums = [20, 50, 40, 25, 30, 10], target = 90
Output: [1, 5]
Explanation:
nums[0] + nums[2] = 20 + 40 = 60 = 90 - 30
nums[1] + nums[5] = 50 + 10 = 60 = 90 - 30
You should return the pair with the largest number.
```

```python
def pairSum(nums: List[int], target: int) -> List[int]:
    diffs = dict()
    best_pair = None
    for i, elem in enumerate(nums):
        if elem in diffs:
            pair = [i, diffs[elem]] if nums[i] < nums[diffs[elem]] else [diffs[elem], i]
            if best_pair:
                best_pair = best_pair if nums[best_pair[1]] > nums[pair[1]] else pair
            else:
                best_pair = pair
        else:
            diff = target - 30 - nums[i]
            diffs[diff] = i

    return best_pair
```
