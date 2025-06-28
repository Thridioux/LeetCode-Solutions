class Solution:
    def maxSubsequence(self, nums, k: int):
        #return any such subsequence of length k with the largest sum
        if k == 0:
            return []
        if k >= len(nums):
            return nums
        # Sort the nums with their indices
        sorted_nums = sorted((num, i) for i, num in enumerate(nums))
        # Get the k largest elements and their indices
        largest_k = sorted_nums[-k:]
        # Sort the largest k elements by their original indices
        largest_k.sort(key=lambda x: x[1])
        # Return only the values of the largest k elements
        return [num for num, _ in largest_k]
    
        