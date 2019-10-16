### Question:
You are on a flight and wanna watch two movies during this flight.
You are given List<Integer> movieDurations which includes all the movie durations.
You are also given the duration of the flight which is d in minutes.
Now, you need to pick two movies and the total duration of the two movies is less than or equal to (d - 30min).

Find the pair of movies with the longest total duration and return they indexes. If multiple found, return the pair with the longest movie.

### Example 1
```
Input: movieDurations = [90, 85, 75, 60, 120, 150, 125], d = 250
Output: [0, 6]
Explanation: movieDurations[0] + movieDurations[6] = 90 + 125 = 215 is the maximum number within 220 (250min - 30min)
```

Two Sum question

```python
def flightDetails(arr, k):
    k-=30
    arr = sorted(arr)
    left = 0
    right = len(arr)-1
    max_val = 0
    i = None
    j = None
    while left<right:
        if arr[left]+arr[right]<=k:
            if max_val < arr[left]+arr[right]:
                max_val = arr[left]+arr[right]
                i = left
                j = right
            left+=1
        else:
            right-=1
    if i is None or j is None:
        return None
    return(arr[i],arr[j])

arr = [90, 85, 75, 60, 120, 150, 125]
k = 250
print(flightDetails(arr,k))
```
