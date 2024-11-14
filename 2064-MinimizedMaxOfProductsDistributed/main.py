class Solution(object):
    def minimizedMaximum(self, n, quantities):
        """
        :type n: int
        :type quantities: List[int]
        :rtype: int
        """
        def canDistribute(max_products):
            stores_needed = sum((quantity + max_products - 1) // max_products for quantity in quantities)
            return stores_needed <= n

        left, right = 1, max(quantities)
        
        # Perform binary search
        while left < right:
            mid = (left + right) // 2
            if canDistribute(mid):
                right = mid  # Try for a smaller max
            else:
                left = mid + 1  # Increase max products per store
        
        return left
            
