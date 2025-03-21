class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid[0])
        
        preRow1 = grid[0][:]
        preRow2 = grid[1][:]
        
        for i in range(1,N):
            preRow1[i] += preRow1[i-1]
            preRow2[i] += preRow2[i-1]
            
        res = float('inf')
        
        for i in range(N):
            top = preRow1[-1] - preRow1[i]
            bottom = preRow2[i-1] if i > 0 else 0
            secondRobot = max(top,bottom)
            res = min(res,secondRobot)
            
        return res
            
        