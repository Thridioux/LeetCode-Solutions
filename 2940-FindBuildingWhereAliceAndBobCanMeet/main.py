class Solution:
    def leftmostBuildingQueries(self, heights, queries):
        from collections import defaultdict
        import heapq
        res = [-1]*len(queries)
        groups = defaultdict(list) #r => [(required_height, query_index)]
        
        # preprocess
        for i,q in enumerate(queries):
            l,r = sorted(q)
            
            if l == r or heights[r] > heights[l]:
                res[i] = r
            else:
                h = max(heights[l], heights[r])
                groups[r].append((h,i))
                
        min_heap = []        
        for i,h in enumerate(heights):
            
            for q_h, q_i in groups[i]:
                heapq.heappush(min_heap, (q_h, q_i))
                
            while min_heap and h > min_heap[0][0]:
                _, q_i = heapq.heappop(min_heap)
                res[q_i] = i
        
        return res
            