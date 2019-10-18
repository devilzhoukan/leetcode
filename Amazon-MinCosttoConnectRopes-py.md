## 1167. Minimum Cost to Connect Sticks

You have some sticks with positive integer lengths.

You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y.  You perform this action until there is one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.

### Example 1:
```
Input: sticks = [2,4,3]
Output: 14
```

### Example 2:
```
Input: sticks = [1,8,3,5]
Output: 30
```

The interesting part is that there is no space relationship!
WTF

```python
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        N = len(sticks)
        if N < 1:
            return None
        if N == 1:
            return 0
        
        heapq.heapify(sticks)
        
        res = 0
        while (len(sticks) > 1):
            first = heapq.heappop(sticks)
            second = heapq.heappop(sticks)
            temp = first + second
            res += temp
            heapq.heappush(sticks, temp)
            
        return res
```
