class TrieNode:
    def __init__(self):
        self.children = {} # key: char, value: TrieNode
        self.word = False # if the node is the end of a word

class Trie:
    def __init__(self,words) :
        self.root = TrieNode() 
        for w in words:
            curr = self.root
            for c in w:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = True
           
                
class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        # Solution: Prefix Tree(Trie)
        dp = { len(s): 0 }
        trie = Trie(dictionary).root
        
        def dfs(i):
            if i in dp:
                return dp[i]
            
            
            res = 1 + dfs(i+1)
            curr = trie 
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                
                if curr.word:
                    res = min(res, dfs(j+1))
                
            dp[i] = res
            return res
        return dfs(0)
    
# test case1
# s= "leetscode"
# dictionary = ["leet","code"]

s = "sayhelloworld"
dictionary = ["hello","world"]



sol = Solution()
print(sol.minExtraChar(s, dictionary)) # 1, 3
