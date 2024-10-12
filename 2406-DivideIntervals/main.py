class Solution(object):
    def minGroups(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        start, end = [], []
        
        for l,r in intervals:
            start.append(l)
            end.append(r)
            
        start.sort()
        end.sort()
        
        #2pointer approach
        i,j = 0,0
        result = 0
        groups = 0
        
        while i< len(intervals) :
            if start[i] <= end[j]:
                groups += 1
                i += 1
            else:
                groups -= 1
                j += 1
            result = max(result, groups)
            
        return result
        
        
    
