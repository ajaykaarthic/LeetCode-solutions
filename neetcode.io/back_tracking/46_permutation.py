
# https://leetcode.com/problems/permutations/
def permute(nums):
    if not nums:
        return []
    permutations = []
    
    def backtrack(permutation, hashset):
        if len(permutation) == len(nums):
            permutations.append(permutation.copy())
            return
        
        for num in nums:
            if num not in hashset:
                permutation.append(num)
                hashset.add(num)
                backtrack(permutation, hashset)
                permutation.pop()
                hashset.remove(num)

    backtrack([], set())
    return permutations


print(permute([1,2,3]))
