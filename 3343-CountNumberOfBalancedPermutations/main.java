class Solution {
    public int countBalancedPermutations(String num) {
        long MOD = 1_000_000_007L;
        long[] fact;
        long[] invfact;
        private long power(long base, long exp){
            long res = 1;
            base %= MOD;
            while (exp > 0){
                if (exp % 2 == 1){
                    res = (res * base) % MOD;
                    base = (base * base) % MOD; 
                    exp /= 2;
                }
            }
            return res;
        }
        private long modInverse(long a){
            return power(a, MOD - 2);
        }
        
        
    }
}