class Solution:
    def getFinalState(self, nums , k, multiplier):
        import heapq
        res =nums[::]
        min_heap = [(n,i) for i,n in enumerate(nums)]
        heapq.heapify(min_heap)
        
        for _ in range(k):
            n, i = heapq.heappop(min_heap)
            res[i] = n*multiplier
            heapq.heappush(min_heap, (res[i], i))
            
        return res