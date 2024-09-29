import sys
class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        # The printer can only print a sequence of the same character each time.
        # At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.    
        # Given a string s, return the minimum number of turns the printer needed to print it.
        
        n = len(s)
        dp = [[sys.maxsize] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
        
        for l in range(2, n + 1): # l is the length of the substring 
            for i in range(n - l + 1): # i is the starting index of the substring
                j = i + l - 1 # j is the ending index of the substring
                
                #print ith letter separately
                dp[i][j] = 1 + dp[i + 1][j] 
                
                for k in range(i + 1, j + 1):
                    if s[i] == s[k]:
                        dp[i][j] = min(dp[i][j], dp[i][k - 1] + (dp[k+1][j] if j>k else 0))
        
        return dp[0][n - 1]
    
# Time: O(n^3)
# Space: O(n^2)

'''
    a   a   a   b   b   b
  +---+---+---+---+---+---+
a | 1 | 1 | 1 | 2 | 2 | 2 |
  +---+---+---+---+---+---+
a | ∞ | 1 | 1 | 2 | 2 | 2 |
  +---+---+---+---+---+---+
a | ∞ | ∞ | 1 | 2 | 2 | 2 |
  +---+---+---+---+---+---+
b | ∞ | ∞ | ∞ | 1 | 1 | 1 |
  +---+---+---+---+---+---+
b | ∞ | ∞ | ∞ | ∞ | 1 | 1 |
  +---+---+---+---+---+---+
b | ∞ | ∞ | ∞ | ∞ | ∞ | 1 |
  +---+---+---+---+---+---+

'''

s=Solution()
print(s.strangePrinter("aaabbb")) # 2