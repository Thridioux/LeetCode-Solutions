class Solution(object):
    def minTimeToReach(self, moveTime):
        """
        :type moveTime: List[List[int]]
        :rtype: int
        """
        m, n = len(moveTime), len(moveTime[0])
        dp = [[float('inf')] * n for _ in range(m)]
        dp[0][0] = 0 #start with no cost

        for i in range(m):
            for j in range(n):
                if i + 1 < m:
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + moveTime[i][j])
                if j + 1 < n:
                    dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + moveTime[i][j])

        return dp[m - 1][n - 1]
