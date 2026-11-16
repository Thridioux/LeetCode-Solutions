from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        # Build prefix sums: prefix[i] = sum(nums[0..i-1])
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        min_sum = float('inf')

        # Check all subarray lengths from l to r
        for size in range(l, r + 1):
            for i in range(n - size + 1):
                sub_sum = prefix[i + size] - prefix[i]
                if sub_sum > 0 and sub_sum < min_sum:
                    min_sum = sub_sum

        return min_sum if min_sum != float('inf') else -1
