class Solution:
    def wordSubsets(self, words1, words2):
        from collections import defaultdict, Counter
        
        count_2 = defaultdict(int) #initially all 0
        
        for w in words2:
            count_w = Counter(w)
            for c,cnt in count_w.items():
                count_2[c] = max(count_2[c], cnt)
                
        res = []
        
        for w in words1:
            count_w = Counter(w)
            flag = True
            for c,cnt in count_2.items():
                if count_w[c] < cnt:
                    flag = False
                    break
            if flag is True:
                res.append(w)
        
        return res