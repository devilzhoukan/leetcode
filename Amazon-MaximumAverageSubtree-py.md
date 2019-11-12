## 1120. Maximum Average Subtree

Given the root of a binary tree, find the maximum average value of any subtree of that tree.

(A subtree of a tree is any node of that tree plus all its descendants. The average value of a tree is the sum of its values, divided by the number of nodes.)

### Thought

It's easy to calculate the sum in recursion way, so the point here is to record the number of nodes.

```python
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.ans = 0
        def helper(root):
            if not root:
                return [0, 0]
            n1, s1 = helper(root.left)
            n2, s2 = helper(root.right)
            n = n1 + n2 + 1
            s = s1 + s2 + root.val
            self.ans = max(self.ans, s / n)
            return [n, s]
        
        helper(root)
        return self.ans
```

```python
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        res = []
        def maximumAvg_helper(node):
            if not node.left and not node.right:
                val = node.val
                num = 1
                res.append(val)
            elif node.left and not node.right:
                tempVal, tempNum = maximumAvg_helper(node.left)
                val = node.val + tempVal
                num = tempNum + 1
                res.append(float(val) / num)
            elif not node.left and node.right:
                tempVal, tempNum = maximumAvg_helper(node.right)
                val = node.val + tempVal
                num = tempNum + 1
                res.append(float(val) / num)
            else:
                tempValR, tempNumR = maximumAvg_helper(node.right)
                tempValL, tempNumL = maximumAvg_helper(node.left)
                val = node.val + tempValR + tempValL
                num = tempNumR + tempNumL + 1
                res.append(float(val) / num)
            return val, num
                
        totalVal, totalNum = maximumAvg_helper(root)
        return max(res)
```

Almost the same, but the latter one store the result and compare.
It runs faster on leetcode but both time complexity is O(N), space complexity is O(N).

## Amazon version
Given an N-ary tree, find the subtree with the maximum average. Return the root of the subtree.
A subtree of a tree is the node which have at least 1 child plus all its descendants. The average value of a subtree is the sum of its values, divided by the number of nodes.

```
Input:
         20
       /   \
    12      18
  /  |  \   / \
11   2   3 15  8

Output: 18
Explanation:
There are 3 nodes which have children in this tree:
12 => (11 + 2 + 3 + 12) / 4 = 7
18 => (18 + 15 + 8) / 3 = 13.67
20 => (12 + 11 + 2 + 3 + 18 + 15 + 8 + 20) / 8 = 11.125

18 has the maximum average so output 18.
```


Python iteration solution: post-order traversal + store total sum and total number in TreeNode

recursive way: remember: need to store the parameters outside
```python
from collections import deque
class TreeNode:
    def __init__(self, val, children):
        self.val = val
        self.children = children
        self.total_val = val
        self.total_num = 1

class Solution:
    def findmaxavgsubtree2(self, root: 'TreeNode') -> 'TreeNode':

        stack1 = deque([])
        stack2 = deque([])
        stack1.append(root)

        max_avg = float('-inf')
        max_avg_node = None

        while stack1:
            visit = stack1.pop()
            stack2.append(visit)
            for child in visit.children:
                stack1.append(child)

        while stack2:
            visit = stack2.pop()
            # if not leaf node, calculate total value and total number
            if len(visit.children) > 0:
                for child in visit.children:
                    visit.total_val += child.total_val
                    visit.total_num += child.total_num
                cur_avg = visit.total_val/visit.total_num
                if cur_avg > max_avg:
                    max_avg = cur_avg
                    max_avg_node = visit
        return max_avg_node
     
    def find_max_avg_sub(self, root):

        self.avg_max = 0
        self.avg_node = None
        def compute_avg(node):
            if node is None:
                return 0, 0
            count = 1
            curr = node.val
            for i in node.children:
                res = compute_avg(i)
                count += res[1]
                curr += res[0]

            curr_avg = curr / count
            if count > 1 and (curr_avg > self.avg_max):
                self.avg_max = curr_avg
                self.avg_node = node
            print(curr, count, self.avg_max)
            return curr, count
        compute_avg(root)
        return self.avg_node
    

if __name__ == '__main__':

    n4 = TreeNode(11, [])
    n5 = TreeNode(2, [])
    n6 = TreeNode(3, [])
    n7 = TreeNode(15, [])
    n8 = TreeNode(8, [])
    n2 = TreeNode(12, [n4, n5, n6])
    n3 = TreeNode(18, [n7, n8])
    n1 = TreeNode(20, [n2, n3])

    ss = Solution()
    print(ss.findmaxavgsubtree2(n1).val)
    print(ss.find_max_avg_sub(n1).val)
```
time : O(N)  
space : O(N)
