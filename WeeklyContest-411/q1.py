class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # s is binary string and k is integer 
        # a binary string satisfies the k constraint if either it contains at most k 0s or at most k 1s
        # return the number of substrings of s that satisfy the k constraint

        # Approach:
        # 1. Initialize the count to 0
        # 2. Iterate through the string and check if the substring satisfies the k constraint
        # 3. If it satisfies, increment the count
        # 4. Return the count

        count = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                substring = s[i:j]
                if substring.count('0') <= k or substring.count('1') <= k:
                    count += 1
        return count
    
    #test cases
input = "11111"
k = 1
print(Solution().countKConstraintSubstrings(input, k)) # 10