class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary = bin(num)[2:] # [2:] to remove the '0b' prefix
        complement = ''.join(['1' if b == '0' else '0' for b in binary])
        return int(complement, 2)
    
num = 5
print(Solution().findComplement(num)) # 2


    


        
        