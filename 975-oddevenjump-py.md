## 975.Odd Even Jump
hard a google problem

Description is so complex so I put it here

----------
You are given an integer array A.  From some starting index, you can make a series of jumps.  The (1st, 3rd, 5th, ...) jumps in the series are called odd numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even numbered jumps.

You may from index i jump forward to index j (with i < j) in the following way:

During odd numbered jumps (ie. jumps 1, 3, 5, ...), you jump to the index j such that A[i] <= A[j] and A[j] is the smallest possible value.  If there are multiple such indexes j, you can only jump to the smallest such index j.
During even numbered jumps (ie. jumps 2, 4, 6, ...), you jump to the index j such that A[i] >= A[j] and A[j] is the largest possible value.  If there are multiple such indexes j, you can only jump to the smallest such index j.
(It may be the case that for some index i, there are no legal jumps.)
A starting index is good if, starting from that index, you can reach the end of the array (index A.length - 1) by jumping some number of times (possibly 0 or more than once.)

Return the number of good starting indexes.

Exmaple 1:

Input: [10,13,12,14,15]

Output: 2

Explanation: 

From starting index i = 0, we can jump to i = 2 (since A[2] is the smallest among A[1], A[2], A[3], A[4] that is greater or equal to A[0]), then we can't jump any more.  
From starting index i = 1 and i = 2, we can jump to i = 3, then we can't jump any more.  
From starting index i = 3, we can jump to i = 4, so we've reached the end.  
From starting index i = 4, we've reached the end already.  
In total, there are 2 different starting indexes (i = 3, i = 4) where we can reach the end with some number of jumps.  


### Solution
__Monotonic Stack__

Where you jump to is determined only by the state of your current index and the jump number partity.

Use Monotonic stack, let's see it in code
```python
class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        if not A: 
            return 0
        N = len(A)
        
        def make(B):
            # B is sorted here
            ans = [None] * N
            stack = []
            for i in B:
                while stack and i > stack[-1]:
                    ans[stack.pop()] = i
                stack.append(i)
                '''
                  That means, when a new index come in, all the indices less than it, 
                  their (odd/even) next is the new one.
                  So pop them out and push the new one in.                  
                '''
            return ans
        
        B = sorted(range(N), key = lambda i:A[i])  # Should be sorted by the rules
        oddnext = make(B)
        B.sort(key = lambda i:-A[i])
        evennext = make(B)
        
        odd = [False] * N
        even = [False] * N
        odd[-1] = even[-1] = True
        
        for i in range(N-2, -1, -1):
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]
            '''
                Here is the important part
                for good or bad status
                odd[i] = even[oddnext[i]] and even[i] = odd[evennext[i]]
            '''
                
        return sum(odd)
```
