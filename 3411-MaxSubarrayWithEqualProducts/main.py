import math
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        
        for i in range(n):
            prod_val = 1
            gcd_val = nums[i]
            lcm_val = nums[i]
            for j in range(i, n):
                prod_val *= nums[j]
                gcd_val = math.gcd(gcd_val, nums[j])
                lcm_val = math.lcm(lcm_val, nums[j])
                
                if prod_val == gcd_val * lcm_val:
                    max_len = max(max_len, j - i + 1)
                    
        return max_len
