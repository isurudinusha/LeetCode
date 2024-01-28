#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
     
        d = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in d:
                d[key] = [s]
            else:
                d[key].append(s)
        return list(d.values())


        # 2. defaultdict
        # d = collections.defaultdict(list)
        # for s in strs:
        #     key = tuple(sorted(s))
        #     d[key].append(s)
        # return list(d.values())
        


# @lc code=end

