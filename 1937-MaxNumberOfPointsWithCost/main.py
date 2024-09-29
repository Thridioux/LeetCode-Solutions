class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(points), len(points[0])
        row = points[0]

        for r in range(1, ROWS):
            next_row = points[r].copy()
            left , right = [0] * COLS, [0] * COLS

            left[0] = row[0]
            for c in range(1, COLS):
                left[c] = max(row[c], left[c-1] - 1)
            
            right[COLS - 1] = row[COLS - 1]
            for c in range(COLS -2, -1, -1):
                right[c] = max(row[c], right[c+1] - 1)

            for c in range(COLS):
                next_row[c] += max(left[c], right[c])
            row = next_row
        return max(row)
    
# Time: O(N*M)
# Space: O
#Test cases
points = [[1,2,3],[1,5,1],[3,1,1]]

sol = Solution()
print(sol.maxPoints(points)) # 9