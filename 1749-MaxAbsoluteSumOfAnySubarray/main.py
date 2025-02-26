class Solution:
    def maxAbsoluteSum(self, nums):
        min_pre, max_pre = 0, 0
        cur = 0
        res = 0
        for num in nums:
            cur += num
            res = max(res, max(abs(cur - min_pre), abs(cur - max_pre)))
            min_pre = min(min_pre, cur)
            max_pre = max(max_pre, cur)
        return res