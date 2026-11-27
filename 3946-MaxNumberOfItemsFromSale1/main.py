from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        mn = min(price for _, price in items)
        
        # If budget is smaller than the cheapest item, we cannot buy anything.
        if budget < mn:
            return 0
            
        factors = [factor for factor, _ in items]
        
        # cnts[i] = total copies obtained by purchasing item i for the first time
        # (1 purchased copy + 1 free copy for each j != i where factor_i divides factor_j)
        # Notice that for j == i, factor_i % factor_i == 0 is also true,
        # which accounts for the 1 purchased copy itself!
        cnts = [sum(1 for fj in factors if fj % fi == 0) for fi in factors]
        
        # 0/1 Knapsack: f[b] is the max copies obtained by activating a subset of item types
        # with an exact expenditure of b.
        f = [-1] * (budget + 1)
        f[0] = 0
        
        for i in range(n):
            price = items[i][1]
            if price > budget:
                continue
            c = cnts[i]
            for b in range(budget, price - 1, -1):
                if f[b - price] != -1:
                    val = f[b - price] + c
                    if val > f[b]:
                        f[b] = val
                        
        # Any remaining budget can be used to buy additional copies of the cheapest item
        # at price mn (each additional purchase yields exactly 1 copy).
        ans = 0
        for b in range(budget + 1):
            if f[b] != -1:
                ans = max(ans, f[b] + (budget - b) // mn)
                
        return ans
