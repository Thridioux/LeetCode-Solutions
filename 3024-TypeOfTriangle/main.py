class Solution:
    def triangleType(self, nums):
        
        # check if the triangle is valid
        if nums[0] + nums[1] <= nums[2] or nums[1] + nums[2] <= nums[0] or nums[0] + nums[2] <= nums[1]:
            return "none"
        # name the triangle equilateral if all sides are equal
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        # name the triangle isosceles if two sides are equal
        elif nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
            return "isosceles"
        # name the triangle scalene if all sides are different
        else:
            return "scalene"
        