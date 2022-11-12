def get_sum_subarray(arr):
    # [2, 2, 3]
    result = []
    combination = []
    def backtrack(i):
        if i >= len(arr):
            result.append(combination.copy())
            return
        
        combination.append(arr[i])
        backtrack(i + 1)
        
        combination.pop()
        backtrack(i + 1)
    backtrack()
    result_sum = 0
    for i in result:
        print(i)
        result_sum += sum(i) * len(i)
    return result_sum

print(get_sum_subarray([2,2,3]))