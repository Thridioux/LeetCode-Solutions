class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        import collections
        import heapq
        graph = collections.defaultdict(list) # {node: [(nei, prob)]}
        for i, (u, v) in enumerate(edges): # u -> v
            graph[u].append((v, succProb[i])) # {0: [(1, 0.5), (2, 0.2)], 1: [(2, 0.5)]}
            graph[v].append((u, succProb[i]))
        
        queue = [(-1, start_node)]  # We use negative probabilities to simulate a max-heap
        probabilities = [0] * n  # To store the maximum probability to reach each node
        probabilities[start_node] = 1
        
        while queue:
            prob, node = heapq.heappop(queue)
            prob = -prob  # Convert back to positive since we stored it as negative in the heap
            
            if node == end_node:
                return prob  # Return the max probability when reaching the end node
            
            for nei, nei_prob in graph[node]:
                new_prob = prob * nei_prob
                if new_prob > probabilities[nei]:  # Only consider paths with higher probability
                    probabilities[nei] = new_prob
                    heapq.heappush(queue, (-new_prob, nei))  # Push with negative probability for max-heap
            
        return 0  # If no path is found, return 0
    
#test cases
sol = Solution()
print(sol.maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2)) #0.25000
