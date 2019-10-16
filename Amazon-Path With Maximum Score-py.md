Given a matrix with r rows and c columns, find the maximum score of a path starting at [0, 0] and ending at [r - 1, c - 1]. The score of a path is the minimum value in that path. For example, the score of the path 8 → 4 → 5 → 9 is 4.

You can only move either down or right at any point in time.

```
Input:
[[5, 1],
 [4, 5]]
Output: 4
Explanation:
Possible paths:
5 → 1 → 5 => min value is 1
5 → 4 → 5 => min value is 4
Return the max value among minimum values => max(4, 1) = 4.
```

```python
def max_min_path(matrix):
    if not matrix or not matrix[0]:
        return 0

    n, m = len(matrix), len(matrix[0])

    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                dp[i][j] = matrix[i][j]
            elif i == 0:
                dp[i][j] = min(matrix[i][j], dp[i][j - 1])
            elif j == 0:
                dp[i][j] = min(matrix[i][j], dp[i - 1][j])
            else:
                dp[i][j] = min(matrix[i][j], max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]
 ```
