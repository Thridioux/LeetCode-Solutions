class Solution(object):
    def xorAllNums(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        res = 0
        if len(nums2) % 2 == 1:
            for n in nums1:
                res ^= n
        if len(nums1) % 2 == 1:
            for n in nums2:
                res ^= n
        return res
        
        