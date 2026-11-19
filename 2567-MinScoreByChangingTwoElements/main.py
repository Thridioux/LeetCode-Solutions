from typing import List

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        # Since we can change any 2 elements, we can always duplicate an existing
        # element to make the minimum absolute difference (low score) equal to 0.
        # Thus, minimizing the score is equivalent to minimizing the high score
        # (max - min) after removing at most 2 extreme values.
        
        nums.sort()
        return min(
            nums[-1] - nums[2],  # Change the 2 smallest elements
            nums[-2] - nums[1],  # Change 1 smallest and 1 largest element
            nums[-3] - nums[0],  # Change the 2 largest elements
        )

        nums.sort()
        return min(
            nums[-1] - nums[2],  # Change the 2 smallest elements
            nums[-2] - nums[1],  # Change 1 smallest and 1 largest element
            nums[-3] - nums[0],  # Change the 2 largest elements
        )