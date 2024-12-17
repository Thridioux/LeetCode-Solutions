class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        from collections import Counter
        import heapq
        count  = Counter(s)
        max_heap = [ (-ord(c),cnt) for c,cnt in count.items()]
        heapq.heapify(max_heap)
        res = []
        
        while max_heap:
            #state 1
            char, cnt = heapq.heappop(max_heap)
            char = chr(-char)
            cur_cnt = min(repeatLimit, cnt)
            res.append(char*cur_cnt)
            #state 2
            
            if cnt - repeatLimit > 0 and max_heap:
                nxt_char, nxt_cnt = heapq.heappop(max_heap) 
                nxt_char = chr(-nxt_char)
                res.append(nxt_char)
                if nxt_cnt > 1:
                    heapq.heappush(max_heap, (-ord(nxt_char), nxt_cnt-1))
                heapq.heappush(max_heap, (-ord(char), cnt-cur_cnt))
                
        return "".join(res)