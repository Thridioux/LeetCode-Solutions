class Solution(object):
    def minTimeToReach(self, moveTime):
        """
        :type moveTime: List[List[int]]
        :rtype: int
        """
        from heapq import heappush, heappop
        ROWS = len(moveTime)
        COLS = len(moveTime[0])
        times = [[float('inf')] * COLS for _ in range(ROWS)] 
        times[0][0] = 0
        heap = []
        heappush(heap, (0, 0, 0))  # (time, x, y)
        visit = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
        
        while heap:
            t,r,c = heappop(heap)
            if (r,c) in visit:
                continue
            visit.add((r,c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < ROWS and 0 <= nc < COLS):
                    continue
                time = max(times[r][c],moveTime[nr][nc]) + (r + c) % 2 + 1
                if time< times[nr][nc]:
                    times[nr][nc] = time
                    heappush(heap, (time, nr, nc))
                    
        return times[ROWS - 1][COLS - 1]
        