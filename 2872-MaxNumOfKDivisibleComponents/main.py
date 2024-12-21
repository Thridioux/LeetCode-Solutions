class Solution:
    def maxKDivisibleComponents(self, n, edges,values,k):
        from collections import defaultdict
        adj = defaultdict(list)
        
        for n1, n2 in edges: #key:node value:adjacent nodes
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        print(adj)
            
        res = 0
        
        def dfs(cur, parent):
            total = values[cur]
            
            for child in adj[cur]: #traverse all children
                if child != parent:
                    total += dfs(child,cur)
                
            if total % k == 0:
                nonlocal res
                res += 1
            return total
        
        dfs(0,-1) 
        return res
                    
#test cases 

# n = 5
# edges = [[0, 1], [1, 2], [1, 3], [3, 4]]
# values = [4, 1, 3, 2, 6]
# k = 5

# sol = Solution()
# print(sol.maxKDivisibleComponents(n, edges, values, k)) #0


n = 7
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
values = [3,0,6,1,5,2,1]
k = 3

sol = Solution()
print(sol.maxKDivisibleComponents(n, edges, values, k)) #3