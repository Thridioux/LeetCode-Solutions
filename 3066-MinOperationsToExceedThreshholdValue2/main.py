class Solution:
    def minOperations(self, nums, k):
        import heapq
        h = nums
        heapq.heapify(h)
        op = 0
        
        while len(h) > 0 and h[0] < k:
            op += 1
            a = heapq.heappop(h)
            b = heapq.heappop(h)
            
            heapq.heappush(h,min(a, b)*2 + max(a, b))  
            
        return op
        