class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
        #Logic
        #right:1 down:1 left:2 up:2, right:3 down:3 left:4 up:4,
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] # Delta r, Delta c for right, down, left, up
        result = []
        r,c = rStart,cStart
        steps = 1 #steps to move in the current direction
        i=0 #direction index
        while len(result) < rows * cols:
            for _ in range(2):
                dr, dc = directions[i]
                for _ in range(steps):
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r,c])
                    r += dr
                    c += dc
                i = (i+1) % 4
            steps += 1
        
        return result
    


        

        
#test
rows = 5
cols = 6
rStart = 1
cStart = 4

test = Solution()
test.spiralMatrixIII(rows, cols, rStart, cStart) # [[1, 4], [1, 5], [2, 5], [2, 4], [2, 3], [1, 3], [0, 3], [0, 4], [0, 5], [3, 5], [3, 4], [3, 3], [3, 2], [2, 2], [1, 2], [0, 2], [4, 5], [4, 4], [4, 3], [4, 2], [4, 1], [3, 1], [2, 1], [1, 1], [0, 1], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]]

