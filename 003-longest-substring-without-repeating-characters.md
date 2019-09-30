*Longest Substring Without Repeating Characters*

Given a string, find the length of the longest substring without repeating characters.  
Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

思路：
从前往后筛，后面遇到新的用hash看一看有没有重复的，不知道这样算暴力还是简便方法。
遇到重复的，就直接截取到重复的，再往后筛选。
感觉是个O(n)，应该已经很优了

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        alphabet_map = {}
        temp = 0
        i = 0
        # search range is [i, j]
        for j in range(n):
            if s[j] in alphabet_map:
                i = alphabet_map.get(s[j]) + 1
            temp = max(temp, j - i + 1)
            alphabet_map[s[j]] = j
        return temp
```

WA了，'abba'输出了3
bb推到了b，当前的子串里是没有a的，遇到最后的a的时候反而推到map存贮的a（的后一位），导致结果变成了3。  
在a离开子串的时候从map里删掉？但是这个例子可以看出，a离开子串和a根本没有关系，是b的原因。  
一直检测map内所有字母在字串内？不可能。  

这里没想明白，看了一下solution，用了一个比较大小（max）就完事了，也是，其实在不在字串内，就是看alphabet_map.get(s[j])在不在[i, j]内，j右侧不用考虑了，毕竟往右遍历才遇到，那么只有考虑是否小于i，小于i，意味着前一个s[j]不在子串内，i就不用右移了。

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        alphabet_map = {}
        temp = 0
        i = 0
        # search range is [i, j]
        for j in range(n):
            if s[j] in alphabet_map:
                i = max(alphabet_map.get(s[j]) + 1, i)
            temp = max(temp, j - i + 1)
            alphabet_map[s[j]] = j
        return temp
```

Runtime: 76 ms, faster than 87.85% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 13.1 MB, less than 5.51% of Python3 online submissions for Longest Substring Without Repeating Characters.

这内存。。。虽然我都是不管空间复杂度的。。。还是清理一下map好吗？md就26个字母有什么可清理的。。。

就26个字母直接用一个52*1的数组行不行呢，肯定可以，能快么，能省多少内存呢。
写一下试试好了

要用到ascii，这里突然想到可能并不只是字母。。那就直接拉满吧。

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        temp = 0
        i = 0
        index_list = [-1]*128
        # search range is [i, j]
        for j in range(n):
            asc_num = ord(s[j])
            i = max(index_list[asc_num] + 1, i)
            temp = max(temp, j - i + 1)
            index_list[asc_num] = j
        return temp
```

我用的i = max(index_list[asc_num] + 1, i)中间这个+1表示跳过，让后面的index就表示真正的index，增加了可读性，不过这里主要初始化就不能写0了，因为直接存到了index_list里，只有一个字符就会因为+1导致输出是0，直接初始化成-1就好了。

Runtime: 80 ms, faster than 80.83% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 13.4 MB, less than 5.05% of Python3 online submissions for Longest Substring Without Repeating Characters.

## **更 差 了**

----------
今天再做，居然什么都忘了，这个精妙的max也忘了，直到推导一遍才恍然大悟
