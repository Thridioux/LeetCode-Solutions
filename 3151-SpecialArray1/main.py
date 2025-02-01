class Solution:
    def isArraySpecial(self, nums):
        N = len(nums)
        if N == 1:
            return True
        for i in range(1, N):
            if nums[i] % 2 == nums[i - 1] % 2:
                return False
        return True
        