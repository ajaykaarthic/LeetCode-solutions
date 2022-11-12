#https://leetcode.com/problems/combination-sum-ii/
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()
        
        def backtrack(combination, index, target):
            if target == 0:
                combinations.append(combination.copy())
                return
            
            for i in range(index, len(candidates)):
                if (i > index) and (candidates[i] == candidates[i -1]):
                    continue
                
                if target - candidates[i] >= 0:
                    combination.append(candidates[i])
                    print(combination)
                    backtrack(combination, i + 1, target - candidates[i])
                    combination.pop()
        backtrack([], 0, target)
        return combinations
        