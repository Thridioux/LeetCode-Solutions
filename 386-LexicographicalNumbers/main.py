class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        cur = 1
        while len(res)<n:
            res.append(cur)
            
            if cur * 10 <= n:
                cur *= 10
            else:
                while cur % 10 == 9 or cur == n: #if the last digit is 9 or cur is equal to n
                    cur = cur // 10
                cur += 1
        return res
                
#test cases 
print(Solution().lexicalOrder(13)) #[1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]        
        
        
        