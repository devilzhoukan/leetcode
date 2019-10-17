## 957. Prison Cells After N Days

There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

- If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
- Otherwise, it becomes vacant.

(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

### Example 1:
```
Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: 
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
```

### Example 2:
```
Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]
```

### Note:
1. ells.length == 8
2. cells[i] is in {0, 1}
3. 1 <= N <= 10^9

### Thought 

Is this a math problem?

the number of prisons is fixed: 8. So there are 256 possible states, eventually the states repeat into a cycle rather quickly. 


```python
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        next = lambda x: int(x > 0 and x < 7 and cells[x-1] == cells[x+1])
        
        def nextday(cells):
            return [next(i) for i in range(8)]
        
        state = {}
        while N > 0:
            c = tuple(cells)
            if c in state:
                N = N % (state[c] - N)
            state[c] = N
            
            if N >= 1:
                N -= 1
                cells = nextday(cells)
        return cells
```

Time Complexity: O(2^N), where NN is the number of cells in the prison.
Space Complexity: O(2^N * N).
