class Solution(object):
    
        #Logic
        #We have a grid which may contain numbers up to 15
        #Check every 3x3 contigious subgrid such that each row, column, and both diagonals all have the same sum.
        # return the number of magic squares inside the grid
        # Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]] Output: 1

    def is_magic(self,square):
        values =[square[i][j] for i in range(3) for j in range(3)] 

        if sorted(values)!= list(range(1,10)):
            return False
        
        #Check rows,cols and diags 
        rows = [sum(square[i]) for i in range(3)] 
        cols = [sum(square[i][j] for i in range(3)) for j in range(3)]
        diagonals = [square[0][0]+square[1][1]+square[2][2],square[0][2]+square[1][1]+square[2][0]]

        all_sums = rows+ cols+ diagonals

        return len(set(all_sums)) == 1

    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if len(grid)<3 or len(grid[0])<3:
            return 0
        
        count = 0
        
        for i in range(len(grid)-2): #starting points of the rows are the top left corner of the 3x3 subgrid
            for j in range(len(grid[0])-2): 
                #Extract the 3x3 subgrid
                square = [row[j:j+3] for row in grid[i:i+3]]
                if self.is_magic(square):
                    count += 1
        
        return count
    

#Test
grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
test = Solution()
test.numMagicSquaresInside(grid) #1

print(test.numMagicSquaresInside(grid)) #1
        


        


        




