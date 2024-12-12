class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        #Take the gifts array and turn it to a heap
        import heapq
        from math import sqrt
        
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)
        
        for _ in range(k):
            gift = -heapq.heappop(gifts)
           
            heapq.heappush(gifts, -int(sqrt(gift)))
            
        return -sum(gifts)
            