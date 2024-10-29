class Solution(object):
    def maxMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        memo = {}

        # DFS function with memoization
        def dfs(row, col):
            if (row, col) in memo:
                return memo[(row, col)]

            max_moves = 0
            current_val = grid[row][col]
            
            # Possible directions: right-up, right, right-down
            for drow, dcol in [(-1, 1), (0, 1), (1, 1)]:
                new_row, new_col = row + drow, col + dcol
                # Check boundaries and if the new cell value is strictly greater
                if 0 <= new_row < ROWS and new_col < COLS and grid[new_row][new_col] > current_val:
                    max_moves = max(max_moves, 1 + dfs(new_row, new_col))
            
            memo[(row, col)] = max_moves
            return max_moves

        # Compute max moves starting from any cell in the first column
        max_result = 0
        for row in range(ROWS):
            max_result = max(max_result, dfs(row, 0))

        return max_result
