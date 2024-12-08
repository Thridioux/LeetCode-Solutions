class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        import heapq
        inf = float('inf')
        events.sort()
        best_prev = -inf
        best = max(v for _, _, v in events)
        
        h = []
        for s,e,v in events:
            while len(h) > 0 and h[0][0] <= s:
                _, nv = heapq.heappop(h)
                best_prev = max(best_prev, nv)
            heapq.heappush(h, (e+1, v))
            best = max(best, best_prev + v)
            
        return best