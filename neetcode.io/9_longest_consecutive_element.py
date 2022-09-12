class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # set of nums in the list
        num_set = set(nums)
        # To keep track of longest sequence
        longest = 0
        
        for i in nums:
            # for each element in the list check if there's an element on the left
            if (i - 1) not in num_set:
                # To keep track of sequence length
                length = 1
                # Calculating the length of the sequence
                while (i + length) in num_set:
                    length += 1
                longest = max(length, longest)
        return longest