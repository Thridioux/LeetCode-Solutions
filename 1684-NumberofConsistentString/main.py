class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        
        allowed_set = set(allowed)
        count = 0
        for word in words:
            if all(char in allowed_set for char in word): # check if all characters in word are in allowed_set
                count += 1
        return count
# Time complexity: O(N)
# Space complexity : O(1)
#test cases
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]

    
print(Solution().countConsistentStrings(allowed, words))

allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
print(Solution().countConsistentStrings(allowed, words))

allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]
print(Solution().countConsistentStrings(allowed, words))


#another solution

# class Solution(object):
#     def countConsistentStrings(self, allowed, words):
#         """
#         :type allowed: str
#         :type words: List[str]
#         :rtype: int
#         """
#         bit_mask = 0
#         for char in allowed:
#             bit = 1 << (ord(char)-ord('a')) # set the bit at the position of the character in the bit_mask
#             bit_mask = bit_mask | bit
#         count = 0
        
#         res =len(words)
#         for word in words:
#             for c in word:
#                 bit = 1 << (ord(c)-ord('a'))
#                 if bit & bit_mask == 0:
#                     res -= 1
#                     break
#         return res
    
                