class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_or = 0
        for n in nums:
            max_or |= n

        res = [0]  # Use a list to hold the result

        def dfs(i, cur):
            if i == len(nums):
                if cur == max_or:
                    res[0] += 1  # Update the result stored in the list
                return
            # Skip the current element
            dfs(i + 1, cur)
            # Include the current element
            dfs(i + 1, cur | nums[i])

        dfs(0, 0)
        return res[0]
