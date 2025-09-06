from typing import List
class Solution:
    def get(self, num: int) -> int:
        if num == 0:
            return 0
        res = 0
        base = 1
        i = 1
        while True:
            l = 1 << (i - 1) * 2
            r = (1 << i * 2) - 1
            if l > num:
                break
            count = min(num, r) - l + 1
            res += count * base
            base += 1
            i += 1
        return res
    def minOperations(self, queries: List[List[int]]) -> int:
        res = 0 
        for q in queries:
            total_reductions = self.get(q[1]) - self.get(q[0] - 1)
            res += (total_reductions + 1) // 2
        return res
        
        
        