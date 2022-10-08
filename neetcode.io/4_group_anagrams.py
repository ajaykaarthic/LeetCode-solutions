'''
https://leetcode.com/problems/group-anagrams/
49. Group Anagrams
Medium

11986

371

Add to List

Share
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # This dictionary has the count of each anagram and it's corresponding anagram in a list
        result = collections.defaultdict(list)
        
        for words in strs:
            #initializing an empty counter for all alphabets
            count = [0] * 26
            
            for c in words:
                # increment the count of alpha for each word
                count[ord(c) - ord('a')] += 1
            # append the anagram word to the corresponding counters. no of counters increases as per no of words    
            result[tuple(count)].append(words)
            
        return result.values()