class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        def dfs(i, cur_set):
            if i == len(s):
                return 0
            res = 0

            for j in range(i,len(s)):
                substring = s[i:j+1]
                if substring not in cur_set:
                    
                    cur_set.add(s[i:j+1])
                    res = max(res, 1 + dfs(j+1, cur_set))
                    cur_set.remove(s[i:j+1])

            return res
        
        return dfs(0, set())

            
                    