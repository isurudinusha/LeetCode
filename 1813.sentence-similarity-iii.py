#
# @lc app=leetcode id=1813 lang=python3
#
# [1813] Sentence Similarity III

# @lc code=start
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # Split both sentences into words
        words1 = sentence1.split()
        words2 = sentence2.split()

        # Ensure words1 is the longer sentence. If not, swap words1 and words2
        if len(words1) < len(words2):
            words1, words2 = words2, words1

        # While both sentences have words and the first word of both sentences is the same
        while words1 and words2 and words1[0] == words2[0]:
            # Remove the first word from both sentences
            words1.pop(0)
            words2.pop(0)

        # While both sentences have words and the last word of both sentences is the same
        while words1 and words2 and words1[-1] == words2[-1]:
            # Remove the last word from both sentences
            words1.pop()
            words2.pop()

        # If words2 is empty, it means all words in sentence2 are in sentence1 in the same order
        # So, return True if words2 is empty, otherwise return False
        return not words2  
    

      

        
        
# @lc code=end

