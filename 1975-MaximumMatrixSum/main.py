class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        res = 0
        neg_cnt = 0
        mat_min = float('inf')
        
        for row in matrix:
            for n in row:
                res += abs(n)
                mat_min = min(mat_min, abs(n))
                if n < 0:
                    neg_cnt += 1
        
        if neg_cnt & 1: # odd number of negative numbers
            res -= 2*mat_min
            
        return res