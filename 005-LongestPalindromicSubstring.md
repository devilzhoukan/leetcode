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

看了一下教程，我这个叫中心扩展法，还有直接往每个字符之间填入'#'把所有even都转换成odd的算法，想了想，也就是代码好写，不一定快，还要写个变回来的，麻烦。

--------------------------
Recently I am practicing dp, and I find that Longest Palindromic Substring is a hot problem that can also be solved by dp.

Let's try it.

```cpp
class Solution {
public:
    string longestPalindrome(string s) {
        if (s.size() == 0) return s;
        string ans;
        
        int N = s.size();
        vector< vector<bool> > dp (N, vector<bool> (N));
        
        for (int i = N - 1; i >= 0; --i) {
            for (int j = i; j < N; ++j) {
                if (i == j || (s[i] == s[j] && (j - i < 2 || dp[i+1][j-1]))) {
                    dp[i][j] = true;
                    if (ans.size() < j - i + 1) {
                        ans = s.substr(i, j - i + 1);
                    }
                }
                else dp[i][j] = false;
            }
        }
        return ans;
    }
};
```

**DETAIL** here: during our traversal, i <= j. Since dp[i][j] relies on dp[i+1][j-1]. The trick here is to reverse the traversal. Let i start from N-1 to 0;

-------------------------
And of course, there is a recursion way.
(I just copy haoel's here)

```cpp
class Solution {
public:
    void findPalindrome(string s, int left, int right, int& start, int& len) {
        int N = s.size();
        while (left >= 0 && right < N && s[left] == s[right]) {
            left--;
            right++;
        }
        if (right - left - 1 > len) {
            len = right - left - 1;
            start = left + 1;
        }
    }
    string longestPalindrome(string s) {
        int N = s.size();
        if (N <= 1) return s;
        int start = 0;
        int len = 0;
        for (int i = 0; i < N - 1; i++) {
            findPalindrome(s, i, i, start, len);
            findPalindrome(s, i, i+1, start, len);
        }
        
        return s.substr(start, len);
    }
};
```
和我想的一个思想，不过封装到一个函数里去了，原则上说，这个应该是没有dp快的，但是实测比dp快，也许是在这样的判断中失败偏多（终止更快），直接去迭代也没有重复判断，所以反而更快吧。
python version
```python
class Solution:
    def find_palindrome(self, s: str, left, right, start, temp_len):
        N = len(s)
        while left >= 0 and right < N and s[left] == s[right]:
            left -= 1
            right += 1
        if right - left - 1 > temp_len:
            start = left + 1
            temp_len = right - left - 1
        
        return start, temp_len
    
    def longestPalindrome(self, s: str) -> str:
        if not s: return s
        N = len(s)
        start = 0
        temp_len = 0
        for i in range(N):
            start, temp_len = self.find_palindrome(s, i, i, start, temp_len)
            start, temp_len = self.find_palindrome(s, i, i+1, start, temp_len)
            
        return s[start: start+temp_len]
```
