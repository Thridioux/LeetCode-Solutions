class Solution:
    def clearDigits(self, s):
        #delete the first digit and closest non digit to its left
        #init a stack   
        stack = []
        
        for i in range(len(s)):
            if s[i].isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(s[i])
                
        return ''.join(stack)
    

        