class Solution:
    def findTargetSumWays(self, nums,target):
        from collections import defaultdict
        dp = defaultdict(int)
        
        dp[0] = 1 # 1 way to sum to zero with first 0 elements
        
        for i in range(len(nums)):
            next_dp =defaultdict(int)
            for cur_sum, count in dp.items():
                next_dp[cur_sum + nums[i]] += count 
                next_dp[cur_sum - nums[i]] += count
            dp = next_dp
        return dp[target]
        
        