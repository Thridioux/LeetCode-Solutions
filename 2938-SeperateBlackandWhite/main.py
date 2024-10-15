class Solution(object):
    def minimumSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        counter = Counter(s)
        
        # 1. count the number of 1s and 0s
        ones = counter['1']
        zeros = counter['0']
        
        # Iterate right to left and count the number of 0 that have already occurred, whenever you iterate on 1 add that counter to the answer.
        ans = 0
        ones_so_far = 0
        zeros_so_far = 0
        
        for i in range(len(s)-1, -1, -1):
            if s[i] == '1':
                ans += zeros_so_far
                ones_so_far += 1
            else:
                zeros_so_far += 1
                
        return ans
    
    
#test cases
s = "0111"
print(Solution().minimumSteps(s)) #1
        