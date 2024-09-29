class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # an  array of integers nums and an integer k is given
        # power of an array defined as Its maximum element if all of its elements are consecutive and sorted in ascending order.-1 otherwise
        # return the power of all subarrays of length k in nums


        n = len(nums)
        powers = []
        for i in range(n - k + 1):
            subarray = nums[i:i+k]
            subarray_sorted = sorted(subarray)
            is_consecutive = all(subarray_sorted[j] + 1 == subarray_sorted[j + 1] for j in range(k - 1))
            
            if is_consecutive and subarray == sorted(subarray):
                powers.append(max(subarray_sorted))

            else:
                powers.append(-1)

        return powers
                
nums =[1,2,3,4,3,2,5]
k=3
sol = Solution()
print(sol.resultsArray(nums, k)) 