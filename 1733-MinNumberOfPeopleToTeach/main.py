from typing import List
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        cncon = set() #cannot communicate
        for u,v in friendships:
            can_comm = False
            mp = set(languages[u-1])
            for lang in languages[v-1]:
                if lang in mp:
                    can_comm = True
                    break
            
            if not can_comm:
                cncon.add(u-1)
                cncon.add(v-1)

        if not cncon:
            return 0

        cnt = [0] * n
        for person in cncon:
            for lang in languages[person]:
                cnt[lang-1] += 1
                
        max_cnt = 0
        for c in cnt:
            max_cnt = max(max_cnt, c)
        
        return len(cncon) - max_cnt
