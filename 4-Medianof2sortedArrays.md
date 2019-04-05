the first hard i meet

## Median of Two Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

居然限定了时间
先这么看nums1 m个， nums2 n个，中位数在(m+n)/2（或是两边），两个数组一起遍历，小的那边继续过，一直遍历到(m+n)/2，时间复杂度是O(m+n)，不符合要求。

那看到这个log，应该是跟**二分法**有点靠近

          left_part          |        right_part
    A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
    B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]

Searching i in [0,m], to find an object i such that:

$\qquad \text{B}[j-1] \leq \text{A}[i] \ and \ \text{A}[i-1] \leq \text{B}[j], \ where \ j = \frac{m + n + 1}{2} - i$


这里显然就是二分法了
然后有一些细节：  
1. 假定n > m， 不然可能出现j是负值的情况，如果不符合，直接交换保证n > m  
2. 可能出现边界值 i=0, i=m, j=0, j=n ，那么两个不等式有一个不成立，直接保证另一个就行了。 Searching i in [0, m][0,m], to find an object i such that: $(j = 0 \ or \ i = m \ or \ \text{B}[j-1] \leq \text{A}[i]) \ and  \ 
(i = 0 \ or \ j = n \ or \ \text{A}[i-1] \leq \text{B}[j]), \  where \ j = \frac{m + n + 1}{2} - i$

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, m, nums2, n = nums2, n, nums1, m
        if n == 0:
            raise ValueError
        
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums2[j-1] > nums1[i]:
                # i is too small, increase i
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # i is too big, decrease i
                imax = i - 1
            else:
                # i is perfect
                if i == 0: 
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])
                
                if (m + n) % 2 == 1:
                    # odd
                    return max_of_left
                
                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                
                return (max_of_left + min_of_right) / 2
```

Runtime: 56 ms, faster than 100.00% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 13.5 MB, less than 5.11% of Python3 online submissions for Median of Two Sorted Arrays.

基本是抄的代码，也没什么可说的，空间复杂度我也不管了。  

反思：  
二分法想到了，但是没想到是这样用，我先想的是i和j一起二分，但是就凑不到i + j = (m + n + 1) // 2 了，这里i二分搜索，j随着i变化是正解。