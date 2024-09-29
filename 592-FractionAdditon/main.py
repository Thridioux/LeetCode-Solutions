class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        from fractions import Fraction
        
        expression = expression.replace('-', ' -')
        expression = expression.replace('+', ' +')
        expression = expression.split() # ['-1/2', '+1/2']
        
        #loop through the expression and add the fractions
        result = Fraction(0, 1)
        for exp in expression:
            result += Fraction(exp)
        
        return str(result.numerator) + '/' + str(result.denominator)

    
solution = Solution()
print(solution.fractionAddition("-1/2+1/2")) # 0/1
print(solution.fractionAddition("-1/2+1/2+1/3")) # 1/3
print(solution.fractionAddition("1/3-1/2")) # -1/6



      