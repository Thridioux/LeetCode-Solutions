#!/usr/bin/env python3
from typing import List
from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        # The number of rows and columns
        M, N = len(mat), len(mat[0])
        
        # A dictionary to group elements by diagonal
        diagonals = defaultdict(list)
        
        for i in range(M):
            for j in range(N):
                diagonals[i + j].append(mat[i][j])
                
        # The final result array
        result = []
        
        #iterate through the diags
        for i in range(M + N - 1):
            if i % 2 == 0:
                # for even indexed diagonals, reverse the list
                diagonals[i].reverse()

            result.extend(diagonals[i])

        return result
    
    
# Example usage:

sol = Solution()
print(sol.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))