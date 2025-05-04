class Solution:
    def numEquivDominoPairs(self, dominoes) -> int:
        from collections import Counter
        total = 0
        lookup = Counter()
        for x,y in dominoes:
            if x > y:
                x,y = y,x
            total += lookup[(x,y)]
            lookup[(x,y)] += 1
        return total            