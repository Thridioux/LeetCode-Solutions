class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []

        for c in s:
            stack.append(c)
            if (len(stack)>= 2 and (
                (stack[-2] == 'A' and stack[-1] == 'B') or
                (stack[-2] == 'C' and stack[-1] == 'D')


            )):
                stack.pop()
                stack.pop()

             
        return len(stack)
    


    