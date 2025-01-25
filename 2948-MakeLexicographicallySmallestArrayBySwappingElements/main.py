class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        from collections import deque
        groups = [] #list of queues
        num_to_group = {} # nums[i] -> group index
        
        for n in sorted(nums):
            if not groups or abs(n-groups[-1][-1]) >limit:
                groups.append(deque())
            groups[-1].append(n)
            num_to_group[n] = len(groups)-1
            
        res = []
        for n in nums:
            group = groups[num_to_group[n]]
            res.append(group.popleft())
            
        return res
                