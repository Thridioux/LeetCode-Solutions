class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # prefix xor
        prefix_xor = [0]
        for num in arr:
            prefix_xor.append(prefix_xor[-1] ^ num)
            
        res = []
        for left,right in queries:
            res.append(prefix_xor[right+1] ^ prefix_xor[left])
        return res
    
        #another solution
        # for i in range(1,len(arr)):
        #     arr[i] ^= arr[i-1]
        # res = []
        # for left,right in queries:
        #     total = arr[right]
        #     remove = 0 if left == 0 else arr[left-1]
            
        #     res.append(total ^ remove)
        # return res
        