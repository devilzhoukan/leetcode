## 240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

### Example:

Consider the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```

Given target = **5**, return **true**.

Given target = **20**, return **false**.

### Thought

it's somewhat like a binary search if left/top is bigger than value,
value is not in this row/column.
if right/bottom is smaller then value,
value is not in this row/colum.

### Solution

Binary Search is ugly, give it up

#### best one I think

Of course the best way is linear: move on the matrix, 
temp > value, move left or up,
temp < value, move right or down.

The problem is that if you start from top left corner, 
you don't know how to move. So the trick here is to start from
left-down corner.

```python
class Solution:
    def searchMatrix(self, matrix, target):
        class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        height = len(matrix)
        width = len(matrix[0])
        
        row = height - 1
        col = 0
        
        while col < width and row >= 0:
            temp = matrix[row][col]
            if temp > target:
                row -= 1
            elif temp < target:
                col += 1
            else:
                return True
            
        return False
```

Time complexity: O(n+m)
Space : O(1)

#### Divide and Conquer

Like what I thought, but is about smallest and largest:

First, if the array has zero area, it contains no elements and therefore cannot contain target. 
Second, if target is smaller than the array's smallest element (found in the top-left corner) 
or larger than the array's largest element (found in the bottom-right corner), then it definitely is not present.

then recursive

```python
class Solution:
    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False

        def search_rec(left, up, right, down):
            # this submatrix has no height or no width.
            if left > right or up > down:
                return False
            # `target` is already larger than the largest element or smaller
            # than the smallest element in this submatrix.
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False

            mid = left + (right-left)//2

            # Locate `row` such that matrix[row-1][mid] < target < matrix[row][mid]
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            
            return search_rec(left, row, mid-1, down) or search_rec(mid+1, up, right, row-1)

        return search_rec(0, 0, len(matrix[0])-1, len(matrix)-1)
```

Time complexity : O(nlgn)  
Space complexity: O(lgn)  
