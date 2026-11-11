from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0] * (n + 1)
        
        for j in range(1, n + 1):
            # Jump from j - 1: cost is 1^2 = 1
            min_prev = dp[j - 1] + 1
            
            # Jump from j - 2: cost is 2^2 = 4
            if j >= 2:
                min_prev = min(min_prev, dp[j - 2] + 4)
                
            # Jump from j - 3: cost is 3^2 = 9
            if j >= 3:
                min_prev = min(min_prev, dp[j - 3] + 9)
                
            dp[j] = costs[j - 1] + min_prev
            
        return dp[n]
