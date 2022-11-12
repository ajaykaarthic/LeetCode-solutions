# https://leetcode.com/problems/permutations-ii/
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        hashmap = dict()
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
            
        def backtrack(permutation):
            if (len(permutation) == len(nums)):
                    permutations.append(permutation.copy())
                    return
            
            for num in hashmap:
                if hashmap.get(num) > 0:
                    permutation.append(num)
                    hashmap[num] -= 1
                    backtrack(permutation)
                    permutation.pop()
                    hashmap[num] += 1

        backtrack([])
        return permutations