class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        # Check if the number of elements in the original array is equal to m*n
        if m*n != len(original):
            return []
        
        # Initialize the 2D array
        res = []
        
        # Iterate through the original array and construct the 2D array
        for i in range(0, len(original), n): # Increment by n
            res.append(original[i:i+n])
            
        return res
    

    
    