class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        sum = 0
        #Subtract the sum of chalk from k until k is less than the sum of chalk.
        
        for i in range(len(chalk)):
            sum += chalk[i]
            if sum > k:
                return i
        k = k % sum #If k is less than the sum of chalk, then find the remainder of k divided by sum.
        for i in range(len(chalk)):
            if chalk[i] > k:
                return i
            k -= chalk[i]
            
        return 0
    
# Time complexity: O(n)
# Space complexity: O(1)
        
        
#test cases
sol = Solution()
print(sol.chalkReplacer([3,4,1,2], 25)) 