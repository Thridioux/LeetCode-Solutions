class Solution:
    def threeSum(self,nums):
        # sort the list
        nums.sort()
        result = []
        # nums = [ -4, -1, -1, 0,1, 2]
        # sorted nums = [-4, -1, -1, 0, 1, 2]
        for i in range(len(nums)-2): # iterate through the list from the first element to the third last element #why is it -2? because we need at least 3 elements to form a triplet
            if i > 0 and nums[i] == nums[i-1]: # if the current element is the same as the previous element, skip the current element
                continue
            l = i + 1
            r = len(nums) - 1 # r is the last element in the list
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    result.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l+1]: #
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return result
    
# test the solution
nums = [-1, 0, 1, 2, -1, -4]
sol = Solution()
print(sol.threeSum(nums)) # [[-1, -1, 2], [-1, 0, 1]]
