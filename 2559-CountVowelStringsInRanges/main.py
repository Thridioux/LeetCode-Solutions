class Solution:
    def vowelStrings(self, words, queries):
        vowels = set('aeiou')
        
        prefix_count = [0] * (len(words) + 1)
        prev = 0
        for i,w in enumerate(words):
            if w[0] in vowels and w[-1] in vowels:
                prev += 1
            prefix_count[i+1] = prev
            
        res = [0] * len(queries)
        
        for i,q in enumerate(queries):
            l,r = q
            res[i] = prefix_count[r+1] - prefix_count[l]
        return res