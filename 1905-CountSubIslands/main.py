class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        ROWS ,COLS = len(grid1), len(grid1[0])
        visit = set()
        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid2[r][c] == 0 or (r, c) in visit: 
                return True
            visit.add((r, c))
            res = True
            if grid1[r][c] == 0:
                res = False
                
            res = dfs(r + 1, c) & dfs(r - 1, c) & dfs(r, c + 1) & dfs(r, c - 1) & res #any of the dfs return False, res will be False , 
            #   This means that the island in grid2 will only be a "sub-island" if all connected cells match islands in grid1.
            
            return res
        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] == 1 and (r, c) not in visit and dfs(r, c): 
                    count += 1
        return count
    
    