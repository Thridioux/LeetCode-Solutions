class Solution(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)  # Convert list to set for faster lookups
        max_len = 0

        # Iterate over each number in the set
        for num in nums:
            current_streak = 0
            current_num = num
            
            # Keep squaring current number as long as it's in the set
            while current_num in nums:
                current_streak += 1
                current_num = current_num ** 2  # Move to the next square
            
            max_len = max(max_len, current_streak)  # Update max length if current streak is longer

        return max_len if max_len > 1 else -1  # Return -1 if no square streaks of length >1


        
        
        
    
    