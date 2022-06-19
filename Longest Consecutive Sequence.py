# LeetCode 128 - Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence


#sorting array approach :
Time complexity: O(nLogn). 
Auxiliary space : O(1).
  
  
```
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)
```

```
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        ans = 0
        count = 0
        
        nums.sort()
        
        v = []
        v.append(nums[0])
        
        for i in range(len(nums)):
            if (nums[i] != nums[i-1]):
                v.append(nums[i])
                
        for i in range(len(v)):
            if (i > 0  and v[i] == v[i-1] + 1):
                count +=1
                
            else:
                count = 1
            
            ans = max(ans,count)
        
        return ans
```
