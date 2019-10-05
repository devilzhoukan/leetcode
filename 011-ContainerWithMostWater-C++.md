## 11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

![des](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)
Example:
```
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
```

* brute force solution 
recursion:
double for loop, O(n^2)
no need to write.

* recursion optimization  
since you get temp Max area, the index gap must be more than temp / height[i]
but still O(n^2)

* 2 ptr approach
2 ptr from begining and end, must choose the longer one to be left.

it's O(n) now

```C++
class Solution {
public:
    int maxArea(vector<int>& height) {
        int result = 0;
        int l = 0;
        int r = height.size() - 1;
        while (l < r) {
            result = std::max(result, std::min(height[l], height[r]) * (r - l));
            if (height[l] < height[r]) {
                l++;
            }
            else {
                r--;
            }
        }
        return result;
    }
};
```
