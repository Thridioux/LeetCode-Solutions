
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Approach 2: 
        dp = [1000] * (n+1)  #initialize the dp array with a large number We know that n is less than 1000 based on the constraints
        dp[1] = 0 # min number of steps to get 1 "A" is 0

        for i in range(2,n+1):
            for j in range(1, 1 + (i//2) ):
                if i%j == 0:
                    dp[i] = min(dp[i], dp[j] + i//j)
        

        return dp[n] #return the value at the nth index