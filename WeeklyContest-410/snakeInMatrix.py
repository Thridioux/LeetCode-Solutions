class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        """
        :type n: int
        :type commands: List[str]
        :rtype: int
        """
        # Direction vectors for RIGHT, DOWN, LEFT, UP
        directions = {
            "RIGHT": (0, 1),
            "DOWN": (1, 0),
            "LEFT": (0, -1),
            "UP": (-1, 0)
        }
        
        # Start at position (0, 0)
        x, y = 0, 0
        
        
        for command in commands:
            dx, dy = directions[command]
            x += dx
            y += dy
        
        final_position = x * n + y
        return final_position

# Test Cases
n = 2
commands = ["RIGHT", "DOWN"]
test = Solution()
print(test.finalPositionOfSnake(n, commands))  # Expected output: 3

n = 3
commands = ["DOWN", "RIGHT", "UP"]
test = Solution()
print(test.finalPositionOfSnake(n, commands))  # Expected output: 1
