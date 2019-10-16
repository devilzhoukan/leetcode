## 235. Lowest Common Ancestor of a Binary Search Tree

**ATTENTION** it's a BST, which means any in left < root < any in right

```python
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Value of current node or parent node.
        parent_val = root.val

        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # If both p and q are greater than parent
        if p_val > parent_val and q_val > parent_val:    
            return self.lowestCommonAncestor(root.right, p, q)
        # If both p and q are lesser than parent
        elif p_val < parent_val and q_val < parent_val:    
            return self.lowestCommonAncestor(root.left, p, q)
        # We have found the split point, i.e. the LCA node.
        else:
            return root
```

## what if the binary tree is not a BST

I think we need pass children's value whether we get q, p.
The first node get both q, p from it's childern make the answer itself
and pass answer to parent until we get from root, 
or change an answer value outside.

Here is the LeetCode solution:
```python
class Solution:

    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recurse_tree(current_node):

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans
```

The trick of LC solution is:  
don't care the flag is q or p, there is only one flag.
Only the LCA will get both true from childern, even the parent of LCA
will get only one true from LCA.

The disadvantage is that it only works for LCA of 2 node, when the number > 2, 
the right solution is have many flag I think.

Here is my own:
```python
class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node):
            if not node:
                return False, False
            left_p, left_q = helper(node.left)
            right_p, right_q = helper(node.right)
            mid_p = node == p
            mid_q = node == q
            
            flag_p = mid_p or left_p or right_p
            flag_q = mid_q or left_q or right_q
            
            if flag_p and flag_q and self.ans is None:
                self.ans = node
                
            return flag_p, flag_q
        
        helper(root)
        return self.ans
```
