class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        # create a helper function that keeps track of the count and the current clipboard
        cache = {}

        def helper(count,paste): #keep track of how many "A" that we have and the current clipboard
            if count == n:
                return 0
            
            if count > n:
                return 1000 #return a large number to avoid this path I know that n is less than 1000 based on the constraints

            if (count,paste) in cache:
                return cache[(count,paste)]
            #Paste
            res1 = 1 + helper(count+paste, paste) 

            #Copy and Paste
            res2 = 2 + helper(count*2, count) 

            cache[(count,paste)] = min(res1,res2)
            return cache[(count,paste)]
        
        if n == 1:
            return 0
        
        return 1+helper(1,1) #start with 1 "A" and 1 in the clipboard
    
#test case
sol = Solution()
print (sol.minSteps(3)) #3

#Time complexity: O(n^2) because we have to check all the possible combinations of copy and paste
#Space complexity: O(n^2) because we have to store the results in the cache




