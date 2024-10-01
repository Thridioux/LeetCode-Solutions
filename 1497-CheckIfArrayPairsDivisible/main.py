class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        # divide the array into exactly n/2 pairs such that the sum of each pair is divisible by k.
        # return True if it is possible to do so, and False otherwise.
        
        
        #initialize a list to count frequency of each remainder
        
        frequencies = [0]*k
        
        for num in arr:
            remainder = num%k
            if remainder < 0:
                remainder += k
            frequencies[remainder] += 1
            
        if frequencies[0] % 2 != 0: # if the frequency of 0 is odd, then we can't pair them
            return False
        
        #Iterate through the rest of the remainders
        
        for i in range(1, k//2 + 1):
            # When k is even and i is exactly half of k, frequencies must be even
            if i == k - i:
                if frequencies[i] % 2 != 0:
                    return False
            else:
                if frequencies[i] != frequencies[k - i]:
                    return False
        return True
    
    
     