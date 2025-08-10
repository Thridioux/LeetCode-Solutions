from typing import List
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s = sorted(str(n))
        
        for i in range(31):
            power_of_two = 1 << i  # 2^i 

            p_s = sorted(str(power_of_two)) #create the signature for 2^i

            if s == p_s:
                return True

        return False