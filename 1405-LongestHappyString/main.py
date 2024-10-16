class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        # s only contains a, b, c
        # s doesnt contain aaa, bbb, ccc as a substring
        # s contains at most a occurences of a, b occurences of b, c occurences of c
        
        counts = [['a', a], ['b', b], ['c', c]]
        result = []
        
        while True:
            counts.sort(key=lambda x: x[1], reverse=True) # sort by count in descending order [a, b, c]
            
            #try to append the most frequent character
            added = False
            
            for i in range(3):
                char, count = counts[i]
                #if this character has been used in the last two characters, skip
                if len(result)>=2 and result[-1] == char and result[-2] == char:
                    continue
                #if the count for this character is non zero append it to the result
                if count > 0:
                    result.append(char)
                    counts[i][1] -= 1
                    added = True
                    break
                
            if not added:
                break
            
        return ''.join(result)
                
        
       
a = 1
b = 1
c = 7
print(Solution().longestDiverseString(a, b, c)) #ccaccacc
        