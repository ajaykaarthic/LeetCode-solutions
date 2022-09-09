class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_count = {}
        result_list = []
        
        # storing all the nums in a dictionary to track count
        for i in nums:
            number_count[i] = 1 + number_count.get(i,0)
        
        # sorting the dictionary in reverse order
        sorted_dict = sorted(number_count.items(), key=operator.itemgetter(1), reverse = True)
        
        # Append the resultant to a list
        for i in range(k):
            result_list.append(sorted_dict[i][0])
            
        return result_list