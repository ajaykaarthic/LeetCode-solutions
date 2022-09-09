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