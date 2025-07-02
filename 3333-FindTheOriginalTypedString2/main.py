class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9 + 7
        n = len(word)
        
        # Find groups of consecutive identical characters
        groups = []
        i = 0
        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            groups.append(j - i)  # length of this group
            i = j
        
        # Total number of ways without length constraint
        total_ways = 1
        for group_size in groups:
            total_ways = (total_ways * group_size) % MOD
        
        # If k <= number of groups, all ways are valid
        if k <= len(groups):
            return total_ways
        
        # Use DP with prefix sum optimization to count invalid ways (length < k)
        # dp[j] = ways to achieve exactly length j
        dp = [0] * k
        dp[0] = 1
        
        for group_size in groups:
            new_dp = [0] * k
            prefix = [0] * (k + 1)
            
            # Build prefix sum of dp
            for i in range(k):
                prefix[i + 1] = (prefix[i] + dp[i]) % MOD
            
            # For each possible final length j
            for j in range(1, k):
                # We can take 1 to min(group_size, j) characters from current group
                max_take = min(group_size, j)
                
                # Sum dp[j-max_take] + dp[j-max_take+1] + ... + dp[j-1]
                # This is prefix[j] - prefix[max(0, j-max_take)]
                left = max(0, j - max_take)
                new_dp[j] = (prefix[j] - prefix[left] + MOD) % MOD
            
            dp = new_dp
        
        # Count invalid ways (length < k)
        invalid_ways = sum(dp[length] for length in range(len(groups), k)) % MOD
        
        return (total_ways - invalid_ways + MOD) % MOD
                                                  