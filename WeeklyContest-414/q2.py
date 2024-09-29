class Solution(object):
    def findMaximumScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0]*n
        stack = []
        
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                idx = stack.pop()
                dp[i] = max(dp[i], dp[idx] + (i - idx) * nums[idx])
            if stack:
                dp[i] = max(dp[i], dp[stack[-1]] + (i - stack[-1]) * nums[stack[-1]])
            stack.append(i)
        return max(dp)
    
    

# test cases
s = Solution()
print(s.findMaximumScore([4,3,1,3,2])) #16 

        