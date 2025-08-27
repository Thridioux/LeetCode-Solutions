from typing import List
from functools import cache
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        DIRS = [(-1, 1),(1,1),(1,-1),(-1,-1)] #TR, BR, BL, TL
        
        @cache
        def dfs(x, y, direction, turn, target):
            if not (0 <= x < n and 0 <= y < m and grid[x][y] == target):
                return 0
            
            nx, ny = x + DIRS[direction][0], y + DIRS[direction][1]
            max_step = 1 + dfs(nx, ny, direction, turn, 2- target)
            if turn == 0:
                nd = (direction + 1) % 4 # 90 degrees clockwise turn
                nx, ny = x + DIRS[nd][0], y + DIRS[nd][1]
                max_step = max(max_step, 1 + dfs(nx, ny, nd, 1, 2 - target))
            
            return max_step
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    max_len = 0
                    for d in range(4):
                        nx, ny = i + DIRS[d][0], j + DIRS[d][1]
                        max_len = max(max_len, 1 + dfs(nx, ny, d, 0,2))
                        
                    res = max(res, max_len)
        return res