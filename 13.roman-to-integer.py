#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
from collections import OrderedDict
class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = OrderedDict()
        romanDict = {

                    "IV"      :     4,
                    "IX"      :     9,
                    "XL"      :     40,
                    "XC"      :     90,
                    "CD"      :     400,
                    "CM"      :     900,
                    "I"      :     1,
                    "V"      :     5,
                    "X"      :     10,
                    "L"      :    50,
                    "C"      :    100,
                    "D"      :     500,
                    "M"      :     1000
        }
        result = 0
        for key in romanDict.keys():
            while key in s:
                s = s.replace(key, '', 1)
                print(romanDict[key])
                result += romanDict[key]
        return result


        
        
# @lc code=end

