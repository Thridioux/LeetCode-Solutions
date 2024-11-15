class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        #remove prefix
        N =len(arr)
        r = N-1
        while r > 0 and arr[r-1] <= arr[r]:
            r -= 1
        
        res = r
        #remove postfix / middle
        #  l          r
        # [1,2,3,10,9,1,2,3]
        l = 0
        
        #remove middle
        while l < r :
            while r < N and arr[l] > arr[r]:
                r += 1
            res = min(res, r - l - 1)
            if arr[l]> arr[l+1]:
                break
        
            l += 1
        return res 