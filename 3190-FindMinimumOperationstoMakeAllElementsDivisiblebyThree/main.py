from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            if n % 3 != 0:
                result += 1
        return result
        