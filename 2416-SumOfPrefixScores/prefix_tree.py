class PrefixNode:
    def __init__(self):
        self.children = [None]*26
        self.count = 0


class PrefixTree(object):
    def __init__(self):
        self.root = PrefixNode()

    def insert(self, w):
        cur = self.root
        for c in w:
            idx = ord(c) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = PrefixNode()
            cur = cur.children[idx]
            cur.count += 1
        

    def get_score(self,w):
        cur = self.root
        score = 0
        for c in w:
            idx = ord(c) - ord('a')
            if not cur.children[idx]:
                return score
            cur = cur.children[idx]
            score += cur.count
        return score

class Solution(object):
    def sumPrefixScores(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        
        res = []
        prefix_tree = PrefixTree()
        
        for w in words:
            prefix_tree.insert(w)
            
        for w in words:
            res.append(prefix_tree.get_score(w))
            
        
        return res