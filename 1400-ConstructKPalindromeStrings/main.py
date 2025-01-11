class Solution:
    def canConstruct(self, s, k):
        if k > len(s):
            return False
        
        from collections import Counter
        count = Counter(s)
        odd = 0
        for cnt in count.values():
            odd += cnt % 2
            
        return odd <= k