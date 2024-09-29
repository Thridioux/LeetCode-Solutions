class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #Rabin-Karp Algorith
        prefix = 0
        suffix = 0
        base = 29 
        last_index = -1 #-1
        power = 1
        mod= 10**29 +7

        for i, c in enumerate(s):
            char =(ord(c)-ord('a')+1) # a-->1

            prefix = (prefix*base)%mod
            prefix = (prefix+char)%mod
            suffix = (suffix+char*power)%mod
            power = (power*base)%mod

            if prefix ==suffix:
                last_index = i
        suffix = s[last_index+1:]
        return suffix[::-1]+s
            


