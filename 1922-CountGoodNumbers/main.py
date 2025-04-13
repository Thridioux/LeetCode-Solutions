from math import ceil

class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        def custom_pow(x, n):
            if n == 0:
                return 1
            res = 1 
            while n > 1:
                if n % 2:
                    res = (res * x) % MOD
                n = n // 2
                x = (x * x) % MOD
            return (res * x) % MOD

        even = ceil(n / 2.0)
        odd = n // 2

        return (custom_pow(5, even) * custom_pow(4, odd)) % MOD
