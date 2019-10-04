## 904 Fruit Into Basket

In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

### This description sucks 

First thought is recursive is N^2, no need to code.
In fact a little optimization can be much better, when meet the third number, there is no need to try any index in front of it.
Next step starts from this index, so it becomes O(N). It can use group by to make consequent same number into a block, but I doubt 
whether it can be faster because it also need time. But I have to admit that it makes code much easier. 

```python
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        blocks = [(k, len(list(v))) for k, v in itertools.groupby(tree)]
        
        ans = 0
        i = 0
        while i < len(blocks):
            types = set()
            weight = 0
            for j in range(i, len(blocks)):
                n = blocks[j]
                types.add(n[0])
                # print('i=',i,'j=',j, 'n=', n)
                if len(types) >= 3:
                    i = j - 1
                    break
                weight += n[1]
                ans = max(ans, weight)
                if j == len(blocks) - 1:
                    return ans
```

It is somehow ugly

solution 2: Sliding Window

Let's perform a sliding window, keeping the loop invariant that i will be the smallest index for which [i, j] is a valid subarray.
```python
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        ans = 0
        i = 0
        count = collections.Counter()
        for j, x in enumerate(tree):
            count[x] += 1
            while len(count) >= 3:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
            ans = max(ans, j - i + 1)
        return ans 
```

Copy a faster code here, make 1000ms to 800ms (any difference ?)
```python
class Solution:
    
    def totalFruit(self, tree: List[int]) -> int:
        last_fruit = -1
        second_last_fruit = -1
        last_fruit_count = 0
        current_max = 0
        maximum = 0
        
        for fruit in tree:
            
            if fruit == last_fruit or fruit == second_last_fruit:
                current_max = current_max + 1
            else:
                current_max = last_fruit_count + 1
                
            if fruit == last_fruit:
                last_fruit_count = last_fruit_count + 1
            else:
                last_fruit_count = 1
                
            if fruit != last_fruit:
                second_last_fruit = last_fruit
                last_fruit = fruit
                
            maximum = max(current_max, maximum)
                
        return maximum
```
