class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        if len(arr1)> len(arr2):
            arr1, arr2 = arr2, arr1
        
        prefix_set = set()
        for n in arr1:
            while n and n not in prefix_set:
                prefix_set.add(n)
                n //= 10
        res = 0
        
        for n in arr2:
            while n and n not in prefix_set:
                n //= 10
            
            if n:
                res = max(res, len(str(n)))
        return res
    
# test case1
arr1 = [123,456,789]
arr2 = [12,34,56,78]
sol = Solution()
print(sol.longestCommonPrefix(arr1, arr2)) # 2
