import random
from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        # Using a 61-bit Mersenne prime and a randomized base for collision-resistant rolling hashing
        MOD = (1 << 61) - 1
        BASE = random.randint(200000, 100000000)
        
        # Precompute prefix polynomial rolling hashes
        H = [0] * (n + 1)
        P = [1] * (n + 1)
        for i in range(n):
            H[i + 1] = (H[i] * BASE + nums[i]) % MOD
            P[i + 1] = (P[i] * BASE) % MOD
            
        def has_unique(L: int) -> bool:
            p_L = P[L]
            counts = {}
            for i in range(n - L + 1):
                h = (H[i + L] - H[i] * p_L) % MOD
                counts[h] = counts.get(h, 0) + 1
            return 1 in counts.values()
            
        # Binary search for the minimum length L with at least one unique subarray
        low, high = 1, n
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if has_unique(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
