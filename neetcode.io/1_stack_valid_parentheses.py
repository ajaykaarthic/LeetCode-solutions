'''
https://leetcode.com/problems/valid-parentheses/ 
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Create a key : value map for each char string
        char_map = { "}" : "{",
                   "]" : "[",
                   ")" : "("}
        
        # Go through the string
        for c in s:
            # Check if the char key in the map, if yes check value equals the stacks top value
            if c in char_map:
                if stack and stack[-1] == char_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False