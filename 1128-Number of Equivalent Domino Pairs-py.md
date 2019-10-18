1128. Number of Equivalent Domino Pairs

Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

```
Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
```

Attention, if there are sevaral same dominoes (# > 2), it calculate multiple times.
So we need store the times a domino appears.

It's still a 2-sum problem.

```python
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        visited = {}
        ans = 0
        for domino in dominoes:
            second, first = domino[1], domino[0]
            if (second, first) in visited:
                ans += visited[(second, first)]
                visited[(second, first)] += 1
            elif (first, second) in visited:
                ans += visited[(first, second)]
                visited[(first, second)] += 1
            else:
                c = tuple(domino)
                visited.update({c: 1})
                
        return ans
```
