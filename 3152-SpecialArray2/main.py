class Solution(object):
    def isArraySpecial(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        import collections
        N = len(nums)
        Q = len(queries)
        
        events = collections.defaultdict(list)
        for index,(s,e) in enumerate(queries):
            events[s].append((index,1))
            events[e].append((index,-1))  
            
        current = set()
        ans = [False]*Q
        
        for qi, t in events[0]:
            if t ==1:
                current.add(qi)
            else:
                if qi in current:
                    current.remove(qi)
                    ans[qi] = True
                
        for i in range(1,N):
            if nums[i] % 2 ==nums[i-1] % 2:
                #this means that we start a new streak
                current = set()
            for qi, t in events[i]:
                if t ==1:
                    current.add(qi)
                else:
                    if qi in current:
                        current.remove(qi)
                        ans[qi] = True
        return ans