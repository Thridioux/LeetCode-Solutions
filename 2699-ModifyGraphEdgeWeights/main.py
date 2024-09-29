class Solution(object):
    def modifiedGraphEdges(self, n, edges, source, destination, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :type target: int
        :rtype: List[List[int]]
        
        """
        
        from collections import defaultdict
        import heapq
        INF = 10**20
        MAX =2 *(10**9)
        e = defaultdict(list)
        add_edges = []
        
        for u, v, w in edges:
            if w == -1:
                add_edges.append([u, v])
                continue
            e[u].append((v, w))
            e[v].append((u, w))
            
        def calc(opt = None):
            if opt is not  None:
                u,v,w = opt
                e[u].append((v, w))
                e[v].append((u, w))
            
            distances = [INF] * n
            h =[]
            
            distances[source] = 0
            heapq.heappush(h, (0, source))
            
            while len(h) > 0:
                d, current = heapq.heappop(h)
                if current == destination:
                    break
                if distances[current] < d:
                    continue
                
                for v,w in e[current]:
                    if distances[v] > distances[current] + w:
                        heapq.heappush(h, (distances[current] + w, v))
                        distances[v] = distances[current] + w
            
            if opt is not None:
                u,v,w = opt
                e[u].pop()
                e[v].pop()
            return distances[destination]
        
        def get_ans(lookup):
            ans =[]
            for u,v,w in edges:
                if w != -1:
                    ans.append([u, v, w])
                else:
                    ans.append([u, v, lookup[(u, v)]])
            return ans
        
        best = calc()
        if best < target:
            return []
        
        if best == target:
            return get_ans(defaultdict(lambda: MAX))
        
        
        progress = defaultdict(lambda: MAX)
        
        for u,v in add_edges:
            best = calc((u, v, 1))
            
            if best ==target:
                progress[(u, v)] = 1
                return get_ans(progress)
            
            if best > target:
                e[u].append((v, 1))
                e[v].append((u, 1))
                progress[(u, v)] = 1
                continue
            
            left =1
            right = MAX
            while left < right:
                mid = (left + right) // 2
                now = calc((u, v, mid))
                if now> target:
                    right = mid -1
                elif now < target:
                    left = mid + 1
                else:
                    left =right = mid
                
            best = calc((u, v, left))
            
            if best == target:
                progress[(u, v)] = left
                return get_ans(progress)
        
        return []
    
#test cases
            
        
            