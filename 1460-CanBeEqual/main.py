class Solution:
    def canBeEqual(self,target,arr) -> bool:
        target.sort()
        arr.sort()
        for i in range(len(target)):
            if target[i] != arr[i]:
                return False
        return True

       
        
        