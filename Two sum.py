from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {}
        for index,element in enumerate(nums):
            rem = target - element
            if rem in output:
                return [output[rem],index]
            output[element] = index
        return []