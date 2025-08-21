from typing import List
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0]) if mat else 0
        res = 0
        height = [0] * n
        
        for i in range(m):
            #calculate heights for the current row
            for j in range(n):
                height[j] = height[j] + 1 if mat[i][j] == 1 else 0
                
            #for each cell, count rectangles ending at (i,j)
            for j in range(n):
                if height[j] > 0:
                    min_height = height[j]
                    for k in range(j, -1, -1):
                        min_height = min(min_height, height[k])
                        if min_height == 0:
                            break
                        res += min_height

        return res
    
