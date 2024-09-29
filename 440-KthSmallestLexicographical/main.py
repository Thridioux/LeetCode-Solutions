class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # return the kth number in lexicographical order
        # so hard to understand
        
        
        cur = 1
        i = 1
        
        def count(cur):
            res = 0
            nei = cur + 1
            while cur <= n:
                res += min(n + 1, nei) - cur
                cur *= 10
                nei *= 10
            return res
        
        while i < k:
            steps = count(cur)
            if i + steps <= k:
                cur = cur + 1
                i = i + steps
            else:
                cur = cur * 10
                i = i + 1
                
        return cur
        
        