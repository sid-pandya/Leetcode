Leetcode 169 - Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


#Sorting Approach
#Time complexity : O(nlgn)
#Space complexity : O(1) or O(n)
```
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
```
