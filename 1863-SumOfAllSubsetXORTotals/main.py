class Solution:
    def subsetXORSum(self, nums):
        def dfs(index, total):
            if index == len(nums):
                return total
            # Include the current number in the XOR sum
            include = dfs(index + 1, total ^ nums[index])
            # Exclude the current number from the XOR sum
            exclude = dfs(index + 1, total)
            return include + exclude
        return dfs(0, 0)
        
        

        