class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones_to_remove = 10
        alice_turn = True
        
        while n >= stones_to_remove:
            n -= stones_to_remove
            stones_to_remove -= 1
            alice_turn = not alice_turn
            
        # If the game stopped on Bob's turn, Bob couldn't make a move, so Alice wins.
        return not alice_turn
