#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,n in enumerate(nums):
                for j in range(i+1,len(nums)):
                    if nums[i]+nums[j] == target:
                        return [i,j]



        
# @lc code=end

