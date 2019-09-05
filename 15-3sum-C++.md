## It's just 3Sum
__But details matter__

No hash version
Though O(n^2), there are some details.

* _Code from haoel_
```C++
vector<vector<int> > threeSum(vector<int> &num) {

    vector< vector<int> > result;
    if(num.size()==0 || num.size()==1 || num.size() == 2) return result;

    //sort the array, this is the key
    sort(num.begin(), num.end());

    int n = num.size();

    for (int i=0; i<n-2; i++) {
        //skip the duplication
        if (i>0 && num[i-1]==num[i]) continue;
        int a = num[i];
        int low = i+1;
        int high = n-1;
        while ( low < high ) {
            int b = num[low];
            int c = num[high];
            if (a+b+c == 0) {
                //got the soultion
                vector<int> v;
                v.push_back(a);
                v.push_back(b);
                v.push_back(c);
                result.push_back(v);
                // Continue search for all triplet combinations summing to zero.
                //skip the duplication
                while(low<n-1 && num[low]==num[low+1]) low++; 
                while(high>0 && num[high]==num[high-1]) high--; 
                low++;
                high--;
            } else if (a+b+c > 0) {
                //skip the duplication
                while(high>0 && num[high]==num[high-1]) high--;
                high--;
            } else{
                //skip the duplication
                while(low<n-1 && num[low]==num[low+1]) low++;
                low++;
            } 
        }
    }
    return result;
}
```

* after viewing some answers on leetcode, my last version
```C++
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        if (nums.size() < 3) {
            return result;
        }
        sort(nums.begin(), nums.end());
        
        int n = nums.size();
        for (int i = 0; i < n - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int a = nums[i];
            int low = i + 1;
            int high = n - 1;
            while (low < high) {
                while (low < high && nums[low] + nums[high] + a > 0) {
                    // while (high > i && nums[high] == nums[high - 1]) high--;
                    high--;
                }
                while (low < high && nums[low] + nums[high] + a < 0) {
                    // while (low < n - 1 && nums[low] == nums[low + 1]) low++;
                    low++;
                }
                if (low < high && nums[low] + nums[high] + a == 0) {
                    // got a solution     
                    result.push_back({a, nums[low], nums[high]});
                    while (low < n - 1 && nums[low] == nums[low + 1]) low++;
                    while (high > i && nums[high] == nums[high - 1]) high--;
                    // will exceed if use high + 1
                    low++;
                    high--;
                }
            }
        }
        return result;
    }
};
```

First one takes 140ms but second one takes 88ms, why?

### vector push
Use v.push_back({..., ..., ...}) is much faster.

### if VS while
In the first solution, it uses if(sum>0) in while(l<r) loop, that's natural. 
However, when it's not a solution, it will jump off the while loop and judge again.
Use while, you can just 'push' it to the approximate range and go on.

but I noticed that many fast anwers don't use while, but in my case it really becomes faster.
