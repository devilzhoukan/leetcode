## 992. Subarrays with K Different Integers
Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.

Example 1:
```
Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: 
[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
```

Use two sliding windows

```python
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        map1 = {}
        map2 = {}
        result = 0
        lPointer = 0
        rPointer = 0
        for v in A:
            if v in map1:
                map1[v] += 1
            else:
                map1[v] = 1
            if v in map2:
                map2[v] += 1
            else:
                map2[v] = 1
                
            while len(map1) > K:
                map1[A[lPointer]] -= 1
                if map1[A[lPointer]] == 0:
                    del map1[A[lPointer]]
                lPointer += 1
                
            while len(map2) >= K:
                map2[A[rPointer]] -= 1
                if map2[A[rPointer]] == 0:
                    del map2[A[rPointer]]
                rPointer += 1
                
            result+= rPointer - lPointer 
        return result
```
