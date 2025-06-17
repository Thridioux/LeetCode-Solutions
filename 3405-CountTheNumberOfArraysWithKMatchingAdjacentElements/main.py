class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        Mx = n + 1
        
        fact = [0] * Mx
        inv_fact = [0] * Mx
        
        def qpow(x, n):
            res = 1
            while n > 0:
                if n & 1:
                    res = res * x % MOD
                x = x * x % MOD
                n >>= 1
            return res
        
        def init():
            fact[0] = 1
            for i in range(1, Mx):
                fact[i] = fact[i - 1] * i % MOD
            
            inv_fact[Mx - 1] = qpow(fact[Mx - 1], MOD - 2)
            for i in range(Mx - 2, -1, -1):
                inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
        init()
        
        def C(n, m):
            if n < m or m < 0:
                return 0
            return fact[n] * inv_fact[m] % MOD * inv_fact[n - m] % MOD
        
        if k >=n:
            return 0

        combinations = C(n - 1, k)
        
        value_assignments = m * qpow(m - 1, n - k - 1) % MOD
        
        return combinations * value_assignments % MOD
        