from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        l = 0 #left pointer 
        r = 1 #right pointer

        for r in range(len(nums)):
            for l in range(r + 1, len(nums)):
                if nums[l] + nums[r] == target:
                    return [l, r]