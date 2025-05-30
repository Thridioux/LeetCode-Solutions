class Solution(object):
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """
        ROWS, COLS = len(box), len(box[0])
        
        for r in range(ROWS):
            i = COLS - 1
            for c in reversed(range(COLS)):
                if box[r][c] == '#':
                    box[r][c], box[r][i] = box[r][i], box[r][c]
                    i -= 1
                elif box[r][c] == '*':
                    i = c - 1
                    
        res = []
        
        for c in range(COLS):
            col = [] # this will be a row after rotation
            for r in reversed(range(ROWS)):
                col.append(box[r][c])
            res.append(col)
            
        return res