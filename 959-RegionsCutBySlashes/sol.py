class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        N = len(grid)
        # create a parent array
        parant = [i for i in range(4*N*N)]
        # find the root of a node
        def find(x):
            if parant[x] != x:
                parant[x] = find(parant[x])
            return parant[x]
        
        # union two nodes
        def union(x, y):
            parant[find(x)] = find(y)

        for r in range(N):
            for c in range(N):
                root = 4*(r*N + c)
                if grid[r][c] == '/':
                    union(root, root+3)
                    union(root+1, root+2) 
                elif grid[r][c] == '\\':
                    union(root, root+1)
                    union(root+2, root+3)
                else:
                    union(root, root+1)
                    union(root+1, root+2)
                    union(root+2, root+3)
                if r+1 < N:
                    union(root+2, root+4*N)
                if c+1 < N:
                    union(root+1, root+4+3)
        
        return sum([parant[i] == i for i in range(4*N*N)])


    
#Test
grid = [" /","/ "]
test = Solution()
print(test.regionsBySlashes(grid)) #2