class Solution:
    def removeOccurrences(self, s, part):
        #remove all occurrences of part from s and return the result
        while part in s:
            s = s.replace(part, '', 1) #replace only the first occurrence of part in s
        return s
    
    
        
        