class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        # Precompute all proper divisors for each length L in [2, n]
        divisors = [[] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(2 * i, n + 1, i):
                divisors[j].append(i)
                
        # cost[i][j] = minimum changes to make substring s[i..j] a semi-palindrome
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                L = j - i + 1
                min_changes = float('inf')
                for d in divisors[L]:
                    m = L // d
                    changes = 0
                    for r in range(d):
                        left = 0
                        right = m - 1
                        while left < right:
                            if s[i + r + left * d] != s[i + r + right * d]:
                                changes += 1
                            left += 1
                            right -= 1
                    if changes < min_changes:
                        min_changes = changes
                cost[i][j] = min_changes
                
        # dp[j]: minimum changes to partition s[0..j-1] into `cnt` semi-palindromes
        # Each semi-palindrome must have length >= 2
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for cnt in range(1, k + 1):
            new_dp = [float('inf')] * (n + 1)
            for j in range(2 * cnt, n + 1):
                for p in range(2 * (cnt - 1), j - 1):
                    val = dp[p] + cost[p][j - 1]
                    if val < new_dp[j]:
                        new_dp[j] = val
            dp = new_dp
            
        return dp[n]

        # Precompute all proper divisors for each length L in [2, n]
        divisors = [[] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(2 * i, n + 1, i):
                divisors[j].append(i)
                
        # cost[i][j] = minimum changes to make substring s[i..j] a semi-palindrome
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                L = j - i + 1
                min_changes = float('inf')
                for d in divisors[L]:
                    m = L // d
                    changes = 0
                    for r in range(d):
                        left = 0
                        right = m - 1
                        while left < right:
                            if s[i + r + left * d] != s[i + r + right * d]:
                                changes += 1
                            left += 1
                            right -= 1
                    if changes < min_changes:
                        min_changes = changes
                cost[i][j] = min_changes
                
        # dp[j]: minimum changes to partition s[0..j-1] into `cnt` semi-palindromes
        # Each semi-palindrome must have length >= 2
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for cnt in range(1, k + 1):
            new_dp = [float('inf')] * (n + 1)
            for j in range(2 * cnt, n + 1):
                for p in range(2 * (cnt - 1), j - 1):
                    val = dp[p] + cost[p][j - 1]
                    if val < new_dp[j]:
                        new_dp[j] = val
            dp = new_dp
            
        return dp[n]