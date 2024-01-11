#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        rev_s = s[::-1]
        
        return True if s==rev_s else False

 
        
# @lc code=end

