#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = Counter(nums)
        sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        top_k_keys = [key for key, _ in sorted_dict[:k]]
        return top_k_keys
    
        #return [x[0] for x in Counter(nums).most_common(k)]
        
        
# @lc code=end

