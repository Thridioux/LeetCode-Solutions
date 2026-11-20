from collections import defaultdict
from typing import List

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = defaultdict(int)
        
        # dp[v] represents the maximum length of consecutive elements ending at v.
        # For each element x, it can either become x + 1 or remain x.
        # Updating dp[x + 1] before dp[x] ensures that the current element
        # is only used once in any consecutive sequence.
        for x in nums:
            dp[x + 1] = dp[x] + 1
            dp[x] = dp[x - 1] + 1
            
        return max(dp.values())
