Leetcode 169 - Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

#HashTable (Dictionary) Approach
#Time Complexity: O(N)
#Space Complexity: O(N)

```
class Solution:
    def majorityElement(self, nums):
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        count = 0
        for key in d:
            if d[key] > (len(nums)//2):
                count = 1
                return key
        if(count == 0):
            return -1
```

---------------OR----------------------

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
