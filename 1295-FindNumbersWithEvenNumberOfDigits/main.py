class Solution:
    def findNumbers(self, nums) -> int:
        N = len(nums)
        ans = 0
        for i in range(N):
            if len(str(nums[i])) % 2 == 0:
                ans += 1
        return ans