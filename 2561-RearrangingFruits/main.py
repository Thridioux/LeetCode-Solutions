from typing import List
from collections import Counter
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        #Step 1: Count the frequency of each fruit in both baskets
        freq = Counter(basket1)
        freq.subtract(Counter(basket2))
        
        #Step2 : Identify fruits that need to be swapped
        to_swap = []
        for fruit_cost, count in freq.items():
            if count % 2 != 0:
                return -1
            
            for _ in range(abs(count) // 2):
                to_swap.append(fruit_cost)
                
        to_swap.sort()
        
        #Step 3: Calculate the minimum cost of swapping
        min_overall_fruit = min(basket1 + basket2)
        cost = 0
        
        #pair smallest excess fruit with largest ones

        for i in range(len(to_swap) // 2):
            #option 1 : direct swap cost
            direct_swap_cost = to_swap[i]
            #option 2 : indirect swap via the cheapest fruit
            indirect_swap_cost = 2 * min_overall_fruit
            
            cost += min(direct_swap_cost, indirect_swap_cost)
            
        return cost     