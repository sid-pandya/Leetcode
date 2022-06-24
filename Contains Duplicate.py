# LeetCode - 217 : Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# hash set approach
Time complexity: O(N),
Memory: O(N) 
```
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = set()
        for i in nums:
            if i in h:
                return True
            h.add(i)
        return False
```

# Method 3 -- Set solution for python
# Time Complexity: O(N)
```
        h =  set(nums)
        if len(nums) == len(h):
            return False
        return True
```
Or
```
    return len(nums) != len(set(nums))
```
