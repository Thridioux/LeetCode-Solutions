class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        operations ={
            '+': lambda x, y: x+y,
            '-': lambda x, y: x-y,
            '*': lambda x, y: x*y
        }
        
        def backtrack(left,right):
            res = []
            
            for i in range(left,right+1):
                op = expression[i]
                if op in operations:
                    nums1 = backtrack(left,i-1)
                    nums2 = backtrack(i+1,right)
                    
                    for num1 in nums1:
                        for num2 in nums2:
                            res.append(operations[op](num1,num2))
            if res == []:
                res.append(int(expression[left:right+1]))
                
            return res
        
        return backtrack(0,len(expression)-1)