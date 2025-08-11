from typing import List
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        powers = []
        
        for i in range(30): # n is up to 10 to the power of 9 , so max 30bits
            if (n >> i) & 1:
                powers.append(1 << i) #or 2**i
        
        answers = []
        for left,right in queries:
            product = 1
            for i in range(left, right + 1):
                product = (product * powers[i]) % MOD
            answers.append(product)
            
        return answers

   

        
        