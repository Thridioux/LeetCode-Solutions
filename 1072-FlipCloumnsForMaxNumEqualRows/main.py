class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        count = defaultdict(int)
        
        for row in matrix:
            row_key = tuple(row)
            if row[0]:
                row_key = tuple([0 if n else 1 for n in row])

            count[row_key] += 1
            
        return max(count.values())
        