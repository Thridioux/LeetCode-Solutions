class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        ## XOR start and goal to get a number where the differing bits are set to 1
        xor_result = start ^ goal 
        flips = bin(xor_result).count('1')
        
        return flips
    
# Time complexity: O(N)
# Space complexity : O(1)
#test cases
start = 3
goal = 4
#expected output : 0
print(Solution().minBitFlips(start, goal))
               
        

        
            

        