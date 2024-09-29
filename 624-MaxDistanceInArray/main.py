class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        #arrays are given ascending order
        #get the first and last element of first array to compare with other arrays
        #if the second array has the last element greater than the first array's last element then update the max_val
        #if the second array has the first element less than the first array's first element then update the min_val
        #find the maximum difference between the max_val and min_val
        #return the result
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        result = 0
        for i in range(1, len(arrays)):
            result = max(result, max(abs(arrays[i][-1] - min_val), abs(max_val - arrays[i][0])))
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
        return result
    

