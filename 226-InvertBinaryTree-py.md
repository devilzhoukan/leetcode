## Invert Binary Tree

A basic problem, and I even write it in python.


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        else:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root
```

It turns out:  
Runtime: 32 ms, faster than 92.88% of Python3 online submissions for Invert Binary Tree.  
Memory Usage: 13.7 MB, less than 5.41% of Python3 online submissions for Invert Binary Tree.  

The recursive way costs too much memory?
But it's Ok, I don't want to think about it
