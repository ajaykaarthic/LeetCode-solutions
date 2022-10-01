'''
https://leetcode.com/problems/permutation-in-string/

567. Permutation in String
Medium

7236

238

Add to List

Share
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2. 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count = {}
        
        # count of chars in s1
        for i in range(len(s1)):
            count[s1[i]] = 1 + count.get(s1[i], 0)
        
        # count of values in the s1
        match = len(count)
        
        k = len(s1)
        
        l, r = 0, 0
        
        while r < len(s2):
            # if the char in s2 is found in the hashmap decrement the corresponding key's value
            if s2[r] in count:
                count[s2[r]] -= 1
                
                # if the value of a particular key is 0, it implies a char match within the window
                if count[s2[r]] == 0:
                    match -= 1
            
            # increment r if the window size is not yet k
            if r - l + 1 < k:
                r += 1
            else:
                if match == 0:
                    return True
                if s2[l] in count:
                    count[s2[l]] += 1
                    if count[s2[l]] == 1: match += 1
                
                # slide the window
                l += 1
                r += 1

        return match == 0