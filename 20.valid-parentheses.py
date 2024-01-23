# @lc app=leetcode id=20 lang=python3
# [20] Valid Parentheses

# @lc code=start

class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty stack
        stack = []
        
        # Define a map where the key is the opening bracket and the value is the closing bracket
        bracket_map = {"(": ")", "[": "]",  "{": "}"}

        # Iterate over each character in the string
        for char in s:
            # If the character is an opening bracket, push it onto the stack
            if char in bracket_map:
                stack.append(char)
            # If the character is a closing bracket, check the top of the stack
            # If the stack is empty or the top of the stack doesn't match the closing bracket, return False
            elif not stack or bracket_map[stack.pop()] != char:
                return False
        # If the stack is empty after iterating over the string, return True
        # If the stack is not empty, return False
        return not stack
    
    
    
# @lc code=end