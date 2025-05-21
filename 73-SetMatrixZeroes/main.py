class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        
        zero_row = False
        zero_col = False
        
        # Check if first row needs to be zeroed
        for j in range(n):
            if matrix[0][j] == 0:
                zero_row = True
                break
        
        # Check if first column needs to be zeroed
        for i in range(m):
            if matrix[i][0] == 0:
                zero_col = True
                break
        
        # Mark rows and columns using first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Zero out marked rows
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        
        # Zero out marked columns
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        
        # Zero first row if needed
        if zero_row:
            for j in range(n):
                matrix[0][j] = 0
        
        # Zero first column if needed
        if zero_col:
            for i in range(m):
                matrix[i][0] = 0