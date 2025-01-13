class Solution:
    def minimumLength(self, s):
        from collections import Counter
        f = Counter(s)
        total = 0
        
        for c in f.keys():
            total += 2- (f[c] % 2)
        return total
        
        
        