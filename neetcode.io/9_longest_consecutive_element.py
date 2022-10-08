'''
https://leetcode.com/problems/longest-consecutive-sequence/
128. Longest Consecutive Sequence
Medium

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''
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