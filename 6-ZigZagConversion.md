## ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

>P   A   H   N  
>A P L S I I G  
>Y   I   R  

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

看到zigzag以为是AVL了，结果一看居然是这种东西。  
不过还是看了一眼答案，和我想的也差不多，就直接填进去就好了。当然这也可以是个数学问题的，不过那样就没什么意义了，而且说到头来都是O(n)

采用的它的sort by row的方法  
```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for i in range(numRows)]
        curRow = 0
        goingDown = False
        
        for c in s:
            rows[curRow].append(c)
            if curRow == 0 or curRow == numRows-1:
                goingDown = not goingDown
            curRow += 1 if goingDown else -1
                
        result = ''
        for row in rows:
            a = ''.join(row)
            result += a
            
        return result
```

Runtime: 72 ms, faster than 93.95% of Python3 online submissions for ZigZag Conversion.
Memory Usage: 13.3 MB, less than 10.35% of Python3 online submissions for ZigZag Conversion.

本来都不想贴上来了，但是还是贴一下吧，毕竟有几个平时很少用但是又很实用的python语句。

>rows = [[] for i in range(numRows)]  

当然还有

>rows = [[0]*numCol for i in range(numRows)] 

python初始化二维数组（list）的方法，真的要用数组直接用numpy不就行了么。

>curRow += 1 if goingDown else -1

python的三目倒是看起来很自然语言

```python
result = ''
        for row in rows:
            a = ''.join(row)
            result += a
```

list转string和string的直接加减，也没什么可说的