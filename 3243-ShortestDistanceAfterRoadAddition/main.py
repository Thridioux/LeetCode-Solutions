class Solution(object):
    def shortestDistanceAfterQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        from collections import deque
        adj = []
        for i in range(n):
            adj.append([i+1])
            
            
        def shortest_path():
            q =deque()
            q.append((0,0))  # (node, distance)
            
            visited = set() # to avoid revisiting the same node
            visited.add((0,0))  # to avoid revisiting the same node
            while q:
                cur,length = q.popleft()
                if cur == n-1:
                    return length
                for neighbor in adj[cur]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append((neighbor,length+1))
            
            
            
        res = []
        for src,dst in queries:
            adj[src].append(dst)
            res.append(shortest_path())
            
        return res