class Solution:
    def fourSum(self, nums, target):
        # sort the list
        nums.sort() # sorted list is    
        result = []
        for i in range(len(nums)-3): # iterate through the list from the first element to the fourth last element
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l = j + 1
                r = len(nums) - 1 # r is the last element in the list
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        result.append([nums[i],nums[j],nums[l],nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
        return result   
# test the solution
nums = [1, 0, -1, 0, -2, 2]
target = 0
sol = Solution()
print(sol.fourSum(nums,target)) # [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
