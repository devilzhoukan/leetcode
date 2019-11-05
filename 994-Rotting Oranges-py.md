# 994. Rotting Oranges

In a given grid, each cell can have one of three values:

- the value 0 representing an empty cell;
- the value 1 representing a fresh orange;
- the value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
If this is impossible, return -1 instead.

### Example 1:
![Image of Example1](https://assets.leetcode.com/uploads/2019/02/16/oranges.png)

```
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```

### Example 2:

```
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, 
because rotting only happens 4-directionally.
```

### Example 3:

```
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
```

## Thought
It's said to be an easy problem. Is it really easy?!

I made many mistakes here, and used some strange tricks. 
Now let me explain the correct natural flow.

### Flow
0. The rotten things spread so a stack or a queue is needed. 
The fastest way is to implement a stack using List([]) and .append(), .pop()
res = -1 and has_One = False

1. Traverse the 2D array, push all rotten oranges(2) to the stack. Once you find a fresh one(1), set has_One to True

2. Check has_One, if not, return 0 since there is no fresh orange.

3. while stack, rot and res+=1. A rotting turn is to pop each orange in stack, let adjacent ones become two and push them in a new stack,
return new stack to change old stack.
Since the last turn of rotting must be pop all orange in stack but nowhere to spread and return a empty stack, 
that means the last turn always doesn't rot. So res starts from -1 to offset it.

4. Return res
