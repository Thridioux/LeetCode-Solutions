class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # Step 1: Convert all numbers to strings for comparison
        nums_str = list(map(str, nums))
        
        # Step 2: Sort numbers based on custom comparator
        # We use the sorted function with a custom key
        nums_str.sort(key=lambda x: x*10, reverse=True)
        
        # Step 3: Concatenate sorted numbers
        largest_num = ''.join(nums_str)
        
        # Step 4: Handle the case where all numbers are zero
        return '0' if largest_num[0] == '0' else largest_num