class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initialize an empty list
        result = [1] * (len(nums))
        
        # multiply all elements on the left of the list nums with the result list
        prefix = 1
        for i in range(len(nums)):
            result[i] *= prefix
            prefix *= nums[i]
        
        # multiply all elements on the right of the list nums with the result list
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result
        
        