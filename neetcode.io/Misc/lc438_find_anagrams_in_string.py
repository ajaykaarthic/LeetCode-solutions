class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = {}
        k = len(p)
        for i in range(k):
            count[p[i]] = 1 + count.get(p[i], 0)
        
        # Total values in a dict
        match = len(count)
        
        l, r = 0, 0
        
        result = []
        while r < len(s):
            if s[r] in count:
                count[s[r]] -= 1
                if count[s[r]] == 0:
                    match -= 1
            if r - l + 1 < k:
                r += 1
            else:
                if match == 0:
                    result.append(l)
                if s[l] in count:
                    count[s[l]] += 1
                    if count[s[l]] == 1:
                        match += 1
                l += 1
                r += 1
        return result
        