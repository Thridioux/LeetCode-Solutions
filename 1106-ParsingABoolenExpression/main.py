class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        s = expression
        self.i = 0
        def helper():
            c = s[self.i] 
            self.i += 1
            if c == 't':
                
                return True
            
            if c == 'f':
                
                return False
            if c == '!':
                self.i += 1
                # !(&(t,f,t))
                res = not helper()
                self.i += 1
                return res
            
            children = []
            self.i += 1
            while s[self.i] != ')':
                if s[self.i] != ',':
                    children.append(helper())
                else:
                    self.i += 1
            self.i += 1
            
            if c == '&':
                return all(children)
            if c == '|':
                return any(children)
        return helper()      