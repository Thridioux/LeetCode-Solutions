class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        
        row_cnt = [0] * ROWS
        col_cnt = [0] * COLS
        
        #preprocess
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    row_cnt[r] += 1
                    col_cnt[c] += 1
        
        res = 0   
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (row_cnt[r] > 1 or col_cnt[c] > 1):
                    res += 1
                    
        return res
        