class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque
        direction = {
            1: [0, 1],
            2: [0, -1],
            3: [1, 0],
            4: [-1, 0]
        }
        ROWS, COLS = len(grid), len(grid[0])
        q = deque([(0, 0, 0)]) # row, col, cost
        min_cost = {(0, 0): 0} # (r,c) -> cost
        
        while q:
            r, c , cost = q.popleft()
            if (r, c) == (ROWS-1, COLS-1):
                return cost
            
            for d in direction:
                dr, dc = direction[d]
                nr, nc = r + dr, c + dc
                n_cost = cost if d ==grid[r][c] else cost + 1
                if (
                    nr < 0 or nc < 0 or nr == ROWS or nc == COLS or 
                    n_cost >= min_cost.get((nr, nc), float('inf'))
                ):
                    continue
                
                min_cost[(nr, nc)] = n_cost
                if d == grid[r][c]:
                    q.appendleft((nr, nc, n_cost))
                else:
                    q.append((nr, nc, n_cost))
                    
        return -1