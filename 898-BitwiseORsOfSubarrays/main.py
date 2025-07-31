from typing import List
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        cur = set()
        
        for x in arr:
            cur = {x} | {y | x for y in cur}
            ans.update(cur)
        return len(ans)
        
        
        
        
        
        