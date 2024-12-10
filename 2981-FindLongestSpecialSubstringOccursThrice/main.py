class Solution(object):
    def maximumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        N = len(s)
        
        current = None
        streak = 0
        
        f = collections.defaultdict(collections.Counter)
        
        def process(c,streak):
            s = streak
            count = 1
            while s > 0:
                f[c][s] += count
                count += 1
                s -= 1
        
        for c in s :
            if c== current:
                streak += 1
            else:
                #previous streak ends
                process(current,streak)
                
                current = c
                streak = 1
                
        process(current,streak)
        
        best  = -1
        for c in f.keys():
            for L in f[c]:
                if f[c][L]>=3:
                    best = max(best,L)
                    
        return best