'''
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 
Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if both strs of same length
        if len(s) != len(t):
            return False
        
        # declare an empty dictionary to keep track of alphabet count
        count_s = {}
        
        # Insert an element to the dict if not available otherwise increase the count of element
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
        
        # Check if char in t is available in s
        for i in t:
            if i in count_s:
                count_s[i] = count_s[i] - 1
        
        # If all the values in the dictionary count_s is 0, it means t is an anagram of s
        for val in count_s.values():
            if val != 0:
                return False
        return True
