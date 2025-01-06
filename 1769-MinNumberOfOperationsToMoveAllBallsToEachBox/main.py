class Solution:
    def minOperations(self, boxes):
        res = [0] * len(boxes)
        
        balls = 0
        moves = 0
        
        for i in range(len(boxes)):
            res[i] = balls + moves
            moves = moves + balls
            balls = balls + int(boxes[i])
            
        balls = 0
        moves = 0
        
        for i in reversed(range(len(boxes))):
            res[i] = res[i] + balls + moves
            moves = moves + balls
            balls = balls + int(boxes[i])
            
        return res
        