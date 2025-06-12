class Solution:
    def maxAdjacentDistance(self, nums) -> int:
        # consider the circular nature of the array and find the maximum difference between adjacent elements
        n = len(nums)
        if n < 2:
            return 0
        max_diff = 0
        for i in range(n):
            next_index = (i + 1) % n
            diff = abs(nums[i] - nums[next_index])
            max_diff = max(max_diff, diff)
        return max_diff
        