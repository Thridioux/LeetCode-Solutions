from typing import List

class Solution:
    def calculate(self, nums: List[int]) -> tuple:
        min_sum = 0
        zero_count = 0
        for ele in nums:
            if ele == 0:
                zero_count += 1
                min_sum += 1
            else:
                min_sum += ele
        return (min_sum, zero_count)

    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        min_sum1, zero_count1 = self.calculate(nums1)
        min_sum2, zero_count2 = self.calculate(nums2)

        if (min_sum1 < min_sum2 and zero_count1 == 0) or (min_sum2 < min_sum1 and zero_count2 == 0):
            return -1
        return max(min_sum1, min_sum2)