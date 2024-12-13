class Solution(object):
    def findScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        rank = [i for i in range(N)]    
        rank.sort(key=lambda x: nums[x])
        
        marked = [False] * N
        score = 0
        
        for r in rank:
            if not marked[r]:
                score += nums[r]
                marked[r] = True
                if r - 1 >= 0:
                    marked[r - 1] = True
                if r + 1 < N:   
                    marked[r + 1] = True
        return score
                    