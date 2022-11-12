# https://leetcode.com/problems/combinations/
def combine( n: int, k: int) -> list[list[int]]:
    combinations = []
    def backtrack(combination, i):
        if len(combination) == k:
            combinations.append(combination.copy())
            return
        
        for i in range(i, n+1):
            combination.append(i)
            backtrack(combination, i + 1)
            combination.pop()
    backtrack([], 1)
    return combinations

print(combine(4, 2))