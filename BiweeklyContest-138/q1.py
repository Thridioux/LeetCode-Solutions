class Solution(object):
    def generateKey(self, num1, num2, num3):
        """
        :type num1: int
        :type num2: int
        :type num3: int
        :rtype: int
        """
        
        
        # Convert numbers to strings and pad with leading zeros to match the length of the longest number
        num1, num2, num3 = map(str, [num1, num2, num3])
        max_len = max(len(num1), len(num2), len(num3))
        num1 = num1.zfill(max_len)
        num2 = num2.zfill(max_len)
        num3 = num3.zfill(max_len)
        
        key = ""
        for i in range(max_len):
            key += str(min(int(num1[i]), int(num2[i]), int(num3[i])))
            
        return int(key)
    
# Time complexity: O(n)
# Space complexity: O(1)
#Test cases:
num1 = 1
num2 = 2
num3 = 3
sol = Solution()
print(sol.generateKey(num1, num2, num3))