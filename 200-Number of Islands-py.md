## 200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
```
Input:
11000
11000
00100
00011

Output: 3
```

BFS:

Linear scan the 2d grid map, if a node contains a '1', 
hen it is a root node that triggers a Breadth First Search. 
Put it into a queue and set its value as '0' to mark as visited node. 
Iteratively search the neighbors of enqueued nodes until the queue becomes empty.

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nrow = len(grid)
        if nrow < 1:
            return 0
        ncol = len(grid[0])
        if ncol < 1:
            return 0
        
        num_islands = 0
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == '1':
                    num_islands += 1
                    # mark as visited
                    grid[r][c] = '2'
                    neighbors = collections.deque()
                    neighbors.append((r, c))
                    while neighbors:
                        row, col = neighbors.popleft()
                        if row - 1 >= 0 and grid[row-1][col] == '1':
                            neighbors.append((row-1, col))
                            grid[row-1][col] = '2';
                        if row + 1 < nrow and grid[row+1][col] == '1':
                            neighbors.append((row+1, col))
                            grid[row+1][col] = '2';
                        if col - 1 >= 0 and grid[row][col-1] == '1':
                            neighbors.append((row, col-1))
                            grid[row][col-1] = '2';
                        if col + 1 < ncol and grid[row][col+1] == '1':
                            neighbors.append((row, col+1))
                            grid[row][col+1] = '2';
        
        return num_islands
```

Time: O(M×N) where M is the number of rows and N is the number of columns.
Space: O(M, N)
