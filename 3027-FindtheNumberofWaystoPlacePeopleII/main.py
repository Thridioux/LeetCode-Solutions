from typing import List
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        n = len(points)
        ans = 0
        
        for i in range(n):
            point_A = points[i]
            yMax = -float("inf")
            
            for j in range(i + 1, n):
                point_B = points[j]
                
                if point_A[1] >= point_B[1]:
                    if point_B[1] > yMax:
                        ans += 1
                        yMax = point_B[1]

        return ans