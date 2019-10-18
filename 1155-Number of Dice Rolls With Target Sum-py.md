You have d dice, and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of f^d total ways) modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.

```
Input: d = 1, f = 6, target = 3
Output: 1
Explanation: 
You throw one die with 6 faces.  There is only one way to get a sum of 3.
```

```
Input: d = 2, f = 6, target = 7
Output: 6
Explanation: 
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
```

```
Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation: 
The answer must be returned modulo 10^9 + 7.
```

### thought

like dp, store the value we can reach now with ways, and calculate what we can reach with
one more die, calculate the ways.

```python
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = collections.defaultdict(int)
        
        for val in range(1, f+1):
            dp[val] += 1
        
        for i in range(d-1):
            temp = dp.copy()
            dp.clear()
            for val in range(1, f+1):                
                for item in temp.items():
                    dp_val = item[0]
                    dp_count = item[1]
                    dp[dp_val + val] += dp_count
        
        return dp[target] % (10**9 + 7)
```

**Attention**

1. Use a defaultdict and avoid judge whether the new sum is in the dic
2. Must have a copy here. First, .items() return a iterator, you can't change the dict when traverse the iterator.
Second, you must clear the dict everytime
3. You can set dp[0] = 1 to start. 

```python
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = collections.defaultdict(int)
        
        dp[0] = 1
        
        for i in range(d):
            temp = dp.copy()
            dp.clear()
            for val in range(1, f+1):                
                for item in temp.items():
                    # print(item)
                    dp_val = item[0]
                    dp_count = item[1]
                    dp[dp_val + val] += dp_count
        
        return dp[target] % (10**9 + 7)
```

