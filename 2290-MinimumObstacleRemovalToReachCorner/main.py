class Solution(object):
    def minimumObstacles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import heapq
        ROWS = len(grid)
        COLS = len(grid[0])
        
        visited = [[False]* COLS for _ in range(ROWS)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up
        
        heap = [(0, 0, 0)] # (obstacles, row, col)
        
        while heap:
            obstacles, x, y = heapq.heappop(heap)
            
            #if we reach the bottom right corner
            if x == ROWS-1 and y == COLS-1:
                return obstacles
            
            #mark current call as visited
            if visited[x][y]:
                continue
            visited[x][y] = True
            
            #explore neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < ROWS and 0 <= ny < COLS and not visited[nx][ny]:
                    #push neighbor into the heap with updated obstacle count
                    heapq.heappush(heap, (obstacles + grid[nx][ny], nx, ny))
                    
        return -1