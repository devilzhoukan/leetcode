## Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

最长回文子串，medium个毛啊，直接看答案吧  
等会，看答案之前还是思考一下。
从前往后遍历，还是用一个hashmap存起来，遇到重复的了，就回去看看前面能不能成一个回文：  
a e b a c d c e c d    
到s[3] = a时重复，这是第一个重复，中间却隔了两个，肯定不是回文。  
到s[6] = c时重复，和s[4] = c重复，这两个差小于3（也就是1或2），满足回文了，看下一个，e和s[3]不一样，回文结束，这一段3个。  
e之前的e在s[1]，也不可能，这个s[7]的e只可能做后面的中心点或者再和之后的回文了。  
s[8]的c满足，s[9]的d满足，最大回文找到。    

这是个O(n)的设想，只过一遍，但感觉复杂的情况我没考虑到，整个思路也很乱。

要不不用hash，每个新遇到的点都当作可能的中心点，去往后找，符合了继续，不符合退出来往后继续假设为中心点去推，感觉是O(n^2)，但又会明显小一些，因为很多都直接排除了。

写的时候感觉aba, abba, abbba, 这样的东西好难受啊。分开考虑吧，一个even，一个odd，aba和abbba就不用管了，中心点往后推会考虑到它的。

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return s
        result = s[0]
        for i in range(len(s)):
            # consider s[i] as center
            # even situation
            for j in range(0, i + 1):
                # print('i, j=', i, j)
                if i+j+1>len(s)-1:
                    break
                if s[i-j] == s[i+j+1]:
                    temp = s[i-j:i+j+2]
                    if len(temp) > len(result):
                        result = temp
                else:
                    break
            # odd situation
            for j in range(0, i):    
                if i-j-1<0 or i+j+1>len(s)-1:
                    break
                # print('i, j=', i, j)            
                if s[i-j-1] == s[i+j+1]:
                    temp = s[i-j-1: i+j+2]
                    if len(temp) > len(result):
                        result = temp
                else:
                    break
        return result
```

Runtime: 2728 ms, faster than 37.32% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 13.2 MB, less than 25.10% of Python3 online submissions for Longest Palindromic Substring.

自己写的粗糙的算法，好歹不是暴力算法，满意了。