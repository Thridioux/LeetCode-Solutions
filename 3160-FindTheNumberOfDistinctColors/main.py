class Solution:
    def queryResults(self, limit, queries):
        from collections import Counter
        N = limit + 1
        f = Counter()
        color = [0] * N
        
        ans = []
        for x, y in queries:
            prev = color[x]
            if prev != 0:
                f[prev] -= 1
                if f[prev] == 0:
                    del f[prev]
            color[x] = y
            f[y] += 1
            ans.append(len(f))
            
        return ans
        