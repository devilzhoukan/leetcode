## 42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

![des_pic](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)

### brute force
for any index in height array，
find max height from left and max height from right，
the height of water in that index will be min(max_left, max_right) - height[index] 

### Dynamic Programming
It's not much like a DP but anyway, it stores what we need in the later for loop.

![dp_pic](https://leetcode.com/problems/trapping-rain-water/Figures/42/trapping_rain_water.png)

let see the code
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        left_ptr = 0
        left_max = 0
        right_ptr = len(height) - 1
        right_max = 0
        trapped = 0
        
        while left_ptr < right_ptr:
            if height[left_ptr] < height[right_ptr]:
                if height[left_ptr] > left_max:
                    left_max = height[left_ptr]
                else:
                    trapped += (left_max - height[left_ptr])
                left_ptr += 1
            
            else:
                if height[right_ptr] > right_max:
                    right_max = height[right_ptr]
                else:
                    trapped += (right_max - height[right_ptr])
                right_ptr -= 1
                
        return trapped
```

Easy to understand, but not perfect.
To make it more like DP, let's see a better code of others.
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        left_ptr = 0
        left_max = 0
        right_ptr = len(height) - 1
        right_max = 0
        trapped = 0
        
        while left_ptr < right_ptr:
            if height[left_ptr] < height[right_ptr]:
                if height[left_ptr] > left_max:
                    left_max = height[left_ptr]
                else:
                    trapped += (left_max - height[left_ptr])
                left_ptr += 1
            
            else:
                if height[right_ptr] > right_max:
                    right_max = height[right_ptr]
                else:
                    trapped += (right_max - height[right_ptr])
                right_ptr -= 1
                
        return trapped
```

Yes, you can traverse just once, keep the left_max and right_max easily after you compare height[left_ptr] and height[right_ptr].

*That's really cool!*
