class Solution:
    def queryResults(self, limit, queries):
        from collections import Counter,defaultdict
        N = limit + 1
        f = Counter()
        colors = defaultdict(lambda: 0)
        
        ans = []
        for x, y in queries:
            prev = colors[x]
            if prev != 0:
                f[prev] -= 1
                if f[prev] == 0:
                    del f[prev]
            colors[x] = y
            f[y] += 1
            ans.append(len(f))
            
        return ans
        