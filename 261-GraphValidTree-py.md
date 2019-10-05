## 261. Graph Valid Tree

Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]  
Output: true  

Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]  
Output: false

I never thought about using a real graph structure to deal with it.
Instead, I use UnionFind.

First version
```python
class Solution:
    def root(self, i, id):
        while i != id[i]:
            id[i] = id[id[i]]
            i = id[i]
        return i
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        id = list(range(n))
        sz = [0] * n
        for pair in edges:
            first, second = pair
            first_root = self.root(first, id)
            second_root = self.root(second, id)
            if (first_root == second_root):
                return False
            if sz[first_root] < sz[second_root]:
                id[first_root] = second_root
                sz[second_root] += sz[first_root]
                # print(first, "->", self.root(first, id), second, "->", self.root(second, id))
            else:
                id[second_root] = id[first_root]
                sz[first_root] += sz[second_root]
                # print(first, "->", self.root(first, id), second, "->", self.root(second, id))
        
        return True
```
And a WA here: 

input  
4   
[[0,1],[2,3]]

Yes, they are not connected to a whole one, so I add this
```python
for i in range(n-1):
            if (self.root(i, id) != self.root(i+1, id)):
                # print("last for:", i, i+1)
                return False
```
And of course, it's really slow. You need to traverse all elements here!

And I found this line of code 
```python
if len(edges) + 1 != n: return False
```

Oh, that's really the basic knowledge of a tree.
