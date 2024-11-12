class Solution(object):
    def maximumBeauty(self, items, queries):
        """
        :type items: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        items.sort() # [price, beauty]
        queries = sorted([(q,i) for i,q in enumerate(queries)]) # [query, index]
        
        res = [0] * len(queries)
        max_bea = 0
        j = 0
        for q,i in queries:
            
            while j < len(items) and items[j][0] <= q:
                max_bea = max(max_bea, items[j][1])
                j += 1
                
            res[i] = max_bea 
        
        return res
                
            