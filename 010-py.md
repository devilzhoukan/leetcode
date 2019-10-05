## 10. Regular Expression Matching
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

### It's really a hard problem

* brute way:

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s       
        first_match = bool(s) and p[0] in {s[0], '.'}        
        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p)))
        else:
            return first_match and self.isMatch(s[1:], p[1:])
```

use dp instead of stupid recursion


* dynamic programming
```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = (i == len(s))
                else:
                    first_match = (i < len(s)) and (p[j] in {s[i], '.'})
                    if j+1 < len(p) and p[j+1] == '*':
                        ans = dp(i, j+2) or (first_match and dp(i+1, j))
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[(i, j)] = ans
            return memo[i, j]
        return dp(0, 0)
```
