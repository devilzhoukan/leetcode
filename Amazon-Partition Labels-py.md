## 763. Partition Labels

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

### Example 1:
```
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
```

Greedy

We need an array last[char] -> index of S where char occurs last. 
Then, let anchor and j be the start and end of the current partition. 
If we are at a label that occurs last at some index after j, 
we'll extend the partition j = last[c]. If we are at the end of the partition (i == j) then we'll append a partition size to our answer, 
and set the start of our new partition to i+1.


```python
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S:
            return []
        last = {c: idx for idx, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for idx, c in enumerate(S):
            j = max(j, last[c])
            if idx == j:
                ans.append(idx - anchor + 1)
                anchor = idx + 1
        return ans
```
