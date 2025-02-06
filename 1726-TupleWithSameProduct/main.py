class Solution:
    def tupleSameProduct(self, nums):
        from collections import defaultdict
        product_cnt = defaultdict(int) # n1 * n2 -> count
        pair_cnt = defaultdict(int) # n1 * n2 -> count of pairs (a, b) and (c, d)
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product = nums[i] * nums[j]
                pair_cnt[product] += product_cnt[product]
                product_cnt[product] += 1
                
        res = 0
        for cnt in pair_cnt.values():
            res += cnt * 8
            
        return res