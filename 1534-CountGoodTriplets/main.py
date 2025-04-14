class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        N = len(arr)
        ans = 0
        
        for i in range(N):
            for j in range(i+1,N):
                for k in range(j+1,N):
                    if (
                        abs(arr[i]-arr[j]) <= a and 
                        abs(arr[j]-arr[k]) <= b and 
                        abs(arr[i]-arr[k]) <= c
                        ):
                        ans += 1
        return ans
    
    
        
        