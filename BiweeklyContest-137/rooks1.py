from itertools import combinations, permutations

class Solution(object):
    def maximumValueSum(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        m, n = len(board), len(board[0])
        max_sum = float('-inf')

        # Generate all combinations of 3 rows
        for rows in combinations(range(m), 3):
            # Generate all combinations of 3 columns
            for cols in combinations(range(n), 3):
                # For each combination of 3 rows and 3 columns, calculate the maximum sum
                for perm in permutations(cols):
                    current_sum = sum(board[rows[i]][perm[i]] for i in range(3))
                    max_sum = max(max_sum, current_sum)

        return max_sum

# Example usage
solution = Solution()

board1 = [[-3, 1, 1, 1], [-3, 1, -3, 1], [-3, 2, 1, 1]]
print(solution.maximumValueSum(board1))  # Expected output: 4

board2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(solution.maximumValueSum(board2))  # Expected output: 15

board3 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
print(solution.maximumValueSum(board3))  # Expected output: 3


# Example usage
solution = Solution()

board1 = [[-3, 1, 1, 1], [-3, 1, -3, 1], [-3, 2, 1, 1]]
print(solution.maximumValueSum(board1))  # Expected output: 4

board2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(solution.maximumValueSum(board2))  # Expected output: 15

board3 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
print(solution.maximumValueSum(board3))  # Expected output: 3
