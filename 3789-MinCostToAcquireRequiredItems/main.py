class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # The cost as a function of type-3 items bought (x3) is piecewise linear,
        # so the minimum must occur at one of the three breakpoints:
        
        # 1. Buy 0 type-3 items: satisfy need1 and need2 separately
        only_separate = need1 * cost1 + need2 * cost2
        
        # 2. Buy min(need1, need2) type-3 items: satisfy the shared need with type-3,
        #    and satisfy the remaining surplus separately
        overlap = min(need1, need2)
        mix = overlap * costBoth + (need1 - overlap) * cost1 + (need2 - overlap) * cost2
        
        # 3. Buy max(need1, need2) type-3 items: satisfy all needs using only type-3
        only_both = max(need1, need2) * costBoth
        
        return min(only_separate, mix, only_both)
