class Solution:
    def countGoodStrings(self, low, high, zero, one):
        mod = 10**9 + 7
        dp = {}
        
        def dfs(lenght):
            if lenght > high:
                return 0
            
            if lenght in dp:
                return dp[lenght]

            dp[lenght] = 1 if lenght >= low else 0
            dp[lenght] += (dfs(lenght + zero)+ dfs(lenght + one)) 
            return dp[lenght] % mod
        
        return dfs(0)