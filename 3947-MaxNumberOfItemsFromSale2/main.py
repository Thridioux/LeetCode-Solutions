from collections import Counter
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        cheapest = min(price for _, price in items)
        
        # If budget cannot afford even the cheapest item, we get 0 items.
        if budget < cheapest:
            return 0
            
        max_f = max(factor for factor, _ in items)
        freq = [0] * (max_f + 1)
        for factor, _ in items:
            freq[factor] += 1
            
        # Sieve to find the number of items that have a factor divisible by `f`
        multiples = [0] * (max_f + 1)
        for f in range(1, max_f + 1):
            if freq[f] > 0:
                for mult in range(f, max_f + 1, f):
                    multiples[f] += freq[mult]
                    
        # Each purchased copy of item i can provide at most 1 free copy of another item j,
        # with at most multiples[factor_i] - 1 such free copies available.
        # Thus, up to (multiples[factor_i] - 1) copies of item i give 2 items for price_i.
        # This deal is worthwhile if and only if price_i < 2 * cheapest.
        cost_count = Counter()
        threshold = 2 * cheapest
        for factor, price in items:
            count = multiples[factor] - 1
            if count > 0 and price < threshold:
                cost_count[price] += count
                
        total = 0
        rem_budget = budget
        
        # Greedily purchase 2-item deals with the lowest price first
        for price in sorted(cost_count.keys()):
            count = cost_count[price]
            can_buy = min(count, rem_budget // price)
            total += can_buy * 2
            rem_budget -= can_buy * price
            
        # Spend any remaining budget on copies of the cheapest item (1 item each)
        total += rem_budget // cheapest
        
        return total
