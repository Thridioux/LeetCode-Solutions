class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import deque
        ROWS,COLS = len(isWater), len(isWater[0])
        q = deque() # (r, c)
        visit = set()
        res = [[-1] * COLS for _ in range(ROWS)]
        
        #enque all water cells
        for r in range(ROWS):
            for c in range(COLS):
                if isWater[r][c] == 1:
                    q.append((r, c))
                    visit.add((r,c))
                    res[r][c] = 0
        #BFS            
        while q:
            r, c = q.popleft() 
            h = res[r][c]
            
            neighbors = [[r+1, c], [r, c+1], [r-1, c], [r, c-1]]
            for nr, nc in neighbors:
                if (nr < 0 or nc < 0 or nr == ROWS or nc == COLS or (nr, nc) in visit):
                    continue   
                q.append((nr,nc))
                visit.add((nr,nc))
                res[nr][nc] = h + 1
                
        return res
                
            