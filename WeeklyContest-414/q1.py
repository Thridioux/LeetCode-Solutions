class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        # Approach: Split the date string by '-' and convert each part to binary
        date = date.split('-')
        year = bin(int(date[0]))[2:]
        month = bin(int(date[1]))[2:]
        day = bin(int(date[2]))[2:]
        
        # return the binary string with dashes 
        
        return year + '-' + month + '-' + day
    
        

# test cases 
s = Solution()
print(s.convertDateToBinary("2080-02-29"))    