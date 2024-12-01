class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # Loop from i = 0 to arr.length, maintaining in a hashTable the array elements from [0, i - 1].
        # on each step of the loop, check if we have seen the element 2 * arr[i] or arr[i] / 2.
        
        hashTable = set()
        
        for i in range(len(arr)):
            if arr[i] * 2 in hashTable or (arr[i] % 2 == 0 and arr[i] // 2 in hashTable):
                return True
            hashTable.add(arr[i])
            
        return False
    