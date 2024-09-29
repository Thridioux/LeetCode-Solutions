from main import Solution
#test cases
n = 4
edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]]
source = 0
destination = 2
target = 6
sol = Solution()
print(sol.modifiedGraphEdges(n, edges, source, destination, target)) #[[1, 0, 4], [1, 2, 3], [2, 3, 5], [0, 3, 1]]


n = 3
edges = [[0,1,-1],[0,2,5]]
source = 0
destination = 2
target = 6
sol = Solution()
print(sol.modifiedGraphEdges(n, edges, source, destination, target)) #[]

n = 5
edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]]
source = 0
destination = 1
target = 5
sol = Solution()
print(sol.modifiedGraphEdges(n, edges, source, destination, target)) #[[4, 1, 1], [2, 0, 1], [0, 3, 1], [4, 3, 1]]
