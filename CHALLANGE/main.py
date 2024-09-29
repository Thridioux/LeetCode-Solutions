class Solution(object):
    def shortestDistanceAfterQueries(self, n, queries):
        dist = [[float('inf')] * n for _ in range(n)] #n=4, dist=[[inf,inf,inf,inf],[inf,inf,inf,inf],[inf,inf,inf,inf],[inf,inf,inf,inf]]
                                                        #queries = [[0,3],[0,2]]
        
        # distance from each node to itself is 0
        for i in range(n):
            dist[i][i] = 0 #dist=[[0,inf,inf,inf],[inf,0,inf,inf],[inf,inf,0,inf],[inf,inf,inf,0]]
            
        result = []
        for u,v in queries: #u=0,v=3
            dist[u][v] = 1 #dist=[[0,inf,inf,1],[inf,0,inf,inf],[inf,inf,0,inf],[inf,inf,inf,0]]
            dist[v][u] = 1 #dist=[[0,inf,inf,1],[inf,0,inf,1],[inf,inf,0,inf],[1,inf,inf,0]]
        
            # Floyd-Warshall algorithm
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

            #record the shortest distance after each query 
            result.append(dist[0][n-1])    
        return result
        
  

# Example usage:
n = 4
queries = [[0, 3], [0, 2]]
solution = Solution()
output = solution.shortestDistanceAfterQueries(n, queries)
print(output)  # Output: [1, 1]
        
