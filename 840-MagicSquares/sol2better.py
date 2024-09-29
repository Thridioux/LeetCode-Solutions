class Solution(object):
    
    
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        
        """
        ROWS, COLS = len(grid), len(grid[0])
        def magic(r,c):
            #ensure 1-9
            values = set()
            for i in range(r,r+3):
                for j in range(c,c+3):
                    if grid[i][j] in values or not (1<=grid[i][j]<=9):
                        return 0
                    values.add(grid[i][j])

            #check rows
            for i in range(r,r+3):
                if sum(grid[i][c:c+3])!=15:
                    return 0
                
                    
                
            #check cols
            for i in range(c,c+3):
                if (grid[r][i]+grid[r+1][i]+grid[r+2][i])!=15:
                    return 0
                
            #check diags
            if (
                grid[r][c]+grid[r+1][c+1]+grid[r+2][c+2]!=15 or 
                grid[r][c+2]+grid[r+1][c+1]+grid[r+2][c]!=15
            ):
                return 0
            return 1
                
        
        
        res = 0
        for r in range (ROWS-2):
            for c in range(COLS-2):
                res += magic(r,c)
                
        return res


    
#Test
grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
test = Solution()

print(test.numMagicSquaresInside(grid)) #1