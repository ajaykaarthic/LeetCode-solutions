class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numMap = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            # If the diff is in the hashmap we return the index of 2 nums
            # Otherwise we add insert the number to the hashmap with it's index
            if diff in numMap:
                return [numMap[diff], i]
            numMap[n] = i