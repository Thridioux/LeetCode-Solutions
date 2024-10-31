class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        """
        :type robot: List[int]
        :type factory: List[List[int]]
        :rtype: int
        """
        robot.sort()
        factory.sort()
        
        n,m = len(robot),len(factory)
        dp =[[float('inf')]*(m+1) for _ in range(n+1)]
        dp[0][0] = 0
        
        for j in range(1,m+1):
            pos, lim = factory[j-1]
            dp[0][j] = 0
            for i in range(1,n+1):
                dp[i][j] = dp[i][j-1]
                diff = 0
                for k in range(1,min(lim,i)+1):
                    diff += abs(robot[i-k]-pos)
                    dp[i][j] = min(dp[i][j],dp[i-k][j-1]+diff)
        return dp[n][m]