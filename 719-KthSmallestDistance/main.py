class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        def count_pairs_with_max_distance(mid):
            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count
        
        low = 0
        high = nums[-1] - nums[0]

        while low<high:
            mid = (low+high)//2 #mid is the maximum distance between two elements
            
            if count_pairs_with_max_distance(mid) < k:
                low = mid + 1
            else:
                high = mid  

        return low
    
# Test Cases
solution = Solution()
print(solution.smallestDistancePair([1,6,1], 3))  