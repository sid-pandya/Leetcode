Leetcode 169 - Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

#HashTable (Dictionary) Approach
#Time Complexity: O(N)
#Space Complexity: O(N)

```
def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d.keys():
                counter = d[i] + 1  
                d[i] = counter   
            else:
                counter = 1
                d[i] = counter   
        for key, values in d.items():
            if values > (len(nums) / 2):
                return key
        return -1
```

#Sorting Approach
#Time complexity : O(nlgn)
#Space complexity : O(1) or O(n)
```
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
```
