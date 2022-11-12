def combinationSum3(k: int, n: int) -> list[list[int]]:
    combinations = []
    def backtrack(combination, index, target):
        if target == 0:
            combinations.append(combination.copy())
            return
        
        for i in range(index, n):
            print(i, combinations)
            for c in combinations:
                if i in c:
                    return
            if target - i >= 0:
                combination.append(i)
                # print(combination)
                backtrack(combination, index + 1, target - i)
                combination.pop()
    backtrack([], 1, n)
    return combinations
print(combinationSum3(3,7))