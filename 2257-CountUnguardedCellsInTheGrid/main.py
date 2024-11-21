class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        grid = [[0] * n for _ in range(m)]
        # 0 = free
        # 1 = guard
        # 2 = wall
        # 3 = guardable
        
        for r, c in guards:
            grid[r][c] = 1
            
        for r, c in walls:
            grid[r][c] = 2

        def mark_guarded_row(r):
            # Process row left-to-right
            guarded = False
            for c in range(n):
                if grid[r][c] == 1:  # Guard
                    guarded = True
                elif grid[r][c] == 2:  # Wall
                    guarded = False
                elif guarded:
                    grid[r][c] = 3  # Mark as guardable

            # Process row right-to-left
            guarded = False
            for c in reversed(range(n)):
                if grid[r][c] == 1:  # Guard
                    guarded = True
                elif grid[r][c] == 2:  # Wall
                    guarded = False
                elif guarded:
                    grid[r][c] = 3  # Mark as guardable

        def mark_guarded_col(c):
            # Process column top-to-bottom
            guarded = False
            for r in range(m):
                if grid[r][c] == 1:  # Guard
                    guarded = True
                elif grid[r][c] == 2:  # Wall
                    guarded = False
                elif guarded:
                    grid[r][c] = 3  # Mark as guardable

            # Process column bottom-to-top
            guarded = False
            for r in reversed(range(m)):
                if grid[r][c] == 1:  # Guard
                    guarded = True
                elif grid[r][c] == 2:  # Wall
                    guarded = False
                elif guarded:
                    grid[r][c] = 3  # Mark as guardable

        # Mark guardable cells for rows
        for r in range(m):
            mark_guarded_row(r)

        # Mark guardable cells for columns
        for c in range(n):
            mark_guarded_col(c)

        # Count unguarded cells
        res = 0
        for row in grid:
            for cell in row:
                if cell == 0:
                    res += 1
                    
        return res
