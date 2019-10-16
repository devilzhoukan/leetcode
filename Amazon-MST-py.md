## 1135. Connecting Cities With Minimum Cost

There are N cities numbered from 1 to N.

You are given connections, where each connections[i] = [city1, city2, cost] represents the cost to connect city1 and city2 together.  (A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)

Return the minimum cost so that for every pair of cities, there exists a path of connections (possibly of length 1) that connects those two cities together.  The cost is the sum of the connection costs used. If the task is impossible, return -1.

Example 1:
```
Input: N = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation: 
Choosing any 2 edges will connect all cities so we choose the minimum 2.
```

Find MST (Minimum spanning tree)

>Kruskal's algorithm:
> 1. Sort connections by cost. Loop connections one by one
> 2. If two cities exists in defferent sets in Union Find, then union them and add their cost. If not, continue.
> 3. Finally, after all connectinos are looped, check if all cities are unioned. If so, return total cost. If not, return -1.

```python 
class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        if len(connections) < N-1:
            return -1
        if N == 1:
            return 0
        
        uf={}
        
        def find(x):
            uf.setdefault(x,x)
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x,y):
            uf[find(x)] = find(y)
            
        res = 0
        
        for c1, c2, cost in sorted(connections, key = lambda x:x[2]):
            if find(c1) != find(c2):
                union(c1,c2)
                res+=cost
                
        if len({find(c) for c in uf})==1:
            return res
        else:
            return -1
```

**Tricks** here
0. Kruskal's algorithm
1. implement simple union-find using python set. the uf.setdefault(x, x) is important here
2. if len({find(c) for c in uf})==1 to judge whether all unioned.
