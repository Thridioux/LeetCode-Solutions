from collections import deque

class Solution:
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        n = len(status)
        
        q = deque(initialBoxes)
        closed = set()
        total = 0
        
        while q:
            curr = q.popleft()
            
            if status[curr] == 0:
                closed.add(curr)
                continue
            
            for open in keys[curr]:
                status[open] = 1
                if open in closed:
                    q.append(open)
                    closed.remove(open)
            
            total += candies[curr]
            for nbr in containedBoxes[curr]:
                q.append(nbr)
        
        return total