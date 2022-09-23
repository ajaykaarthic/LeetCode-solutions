
'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/

3. Longest Substring Without Repeating Characters
Medium

28822

1229

Add to List

Share
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0
        max_substring = 0
        
        for r in range(len(s)):
            # Check if the char is in set: if not increase the count otherwise remove s[l] from the set
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            max_substring = max(max_substring, r - l + 1)
        return max_substring

# Need to revisit below solution
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         max_substring = 0
#         l = 0
#         r = 1
#         if len(s) == 0:
#             return 0
#         if len(s) == 1:
#             return 1
#         while l < r:
#             count = 0
#             for i in range(l, r):
#                 if s[r] == s[i]:
#                     l += 1
#                     r = l + 1
#                     break
#                 count += 1
#             r += 1
#             if count > max_substring:
#                 max_substring = count
#         return max_substring