from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Use sets to track candidates for rows, columns, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # Track empty cells
        empty_cells = []
        
        # Initialize sets with existing numbers
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = int(board[r][c])
                    rows[r].add(num)
                    cols[c].add(num)
                    box_id = (r // 3) * 3 + (c // 3)
                    boxes[box_id].add(num)
                else:
                    empty_cells.append((r, c))
        
        self.solve(board, rows, cols, boxes, empty_cells)
    
    def get_candidates(self, r, c, rows, cols, boxes):
        box_id = (r // 3) * 3 + (c // 3)
        used = rows[r] | cols[c] | boxes[box_id]
        return [num for num in range(1, 10) if num not in used]
    
    def solve(self, board, rows, cols, boxes, empty_cells):
        if not empty_cells:
            return True
        
        # Sort empty cells by number of candidates (most constrained first)
        empty_cells.sort(key=lambda cell: len(self.get_candidates(cell[0], cell[1], rows, cols, boxes)))
        
        r, c = empty_cells[0]
        empty_cells.pop(0)
        
        candidates = self.get_candidates(r, c, rows, cols, boxes)
        if not candidates:
            empty_cells.insert(0, (r, c))
            return False
        
        box_id = (r // 3) * 3 + (c // 3)
        
        for num in candidates:
            # Place the number
            board[r][c] = str(num)
            rows[r].add(num)
            cols[c].add(num)
            boxes[box_id].add(num)
            
            if self.solve(board, rows, cols, boxes, empty_cells):
                return True
            
            # Backtrack
            board[r][c] = '.'
            rows[r].remove(num)
            cols[c].remove(num)
            boxes[box_id].remove(num)
        
        # Put the cell back for future backtracking
        empty_cells.insert(0, (r, c))
        return False