class Solution(object):
    def sumPrefixScores(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        # O(n * l * l) time complexity
        from collections import defaultdict
        res = []
        
        count = defaultdict(int)
        for w in words:
            for i in range(len(w)):
                count[w[:i+1]] += 1
        
        for w in words:
            score = 0
            for i in range(len(w)):
                score += count[w[:i+1]]
            res.append(score)
    
        return res
    
        # better optimized solution
        # O(n * l) time complexity
        # Prefix Tree aka Trie data structure
        
        