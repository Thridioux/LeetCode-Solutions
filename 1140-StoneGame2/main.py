'''Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.'''

class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        dp = {}
    
        def dfs(alice, i, M): #It returns num of stones Alice gets
            if i == len(piles): #if we are out of bounds 
                return 0
            if (alice,i, M) in dp:
                return dp[(alice, i, M)]
            
            res = 0 if alice else float('inf')
            total = 0
            for X in range (1, 2*M + 1): 
                if i + X -1 >= len(piles): 
                    break
                total+= piles[i + X -1]
                if alice: #Alice's turn
                    res = max(res, total + dfs(not alice , i + X, max(M, X)))
                else: #Bob's turn
                    res = min(res, dfs(not alice, i + X, max(M, X)))

            dp[(alice, i, M)] = res
            return res
        return dfs(True, 0, 1)
    
# Time complexity: O(n^2)
# Space complexity: O(n^2)

piles = [2,7,9,4,4]
sol = Solution()
print(sol.stoneGameII(piles)) #10





        