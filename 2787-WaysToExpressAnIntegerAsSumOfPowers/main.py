class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        #dp[j] = number of ways to make sum j 
        dp = [0] * (n + 1)
        dp[0] = 1
        
        #iterate through each possible base number 'i'
        for i in range(1, n + 1):
            val = pow(i, x)
            
            if val > n:
                break
            
            #update dp table for this item 'val'
            # Iterate backwards to use each item at most once 
            for j in range(n, val - 1, -1):
                dp[j] = (dp[j] + dp[j - val]) % MOD

        return dp[n]