class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        # we are looking for the smallest k >= such that:
        # x = num1 - k * num2 >= 0
        
        k = 1
        while True:
            x = num1 - k * num2 
            # if x becomes smaller than k, its impossible to satidfy the condition
            if x < k:
                return -1
            
            if x.bit_count() <= k:
                return k
            k += 1
        return -1
        
        