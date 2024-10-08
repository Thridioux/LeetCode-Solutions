class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        #iterate over the string and keep track of the number of open and close brackets 
        open_brackets = 0
        close_brackets = 0
        for c in s:
            if c == '[':
                open_brackets += 1
            else:
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    close_brackets += 1
                    
        # if the number of open brackets is greater than the number of close brackets
        # swap it with opening bracket close to the end of s
        if open_brackets > close_brackets:
            return (open_brackets + 1) // 2
        else:
            return (close_brackets + 1) // 2

#test the solution
s = Solution()
print(s.minSwaps("][][")) #1
print(s.minSwaps("]]][[[")) #2