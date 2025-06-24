class Solution:
    def findKDistantIndices(self, nums, key: int, k: int):
        #return a list of indices in increasing order such that the absolute difference between each index and the index of the key is at most k
        
        answer = []
        key_indices = [i for i, num in enumerate(nums) if num == key]
        
        for i in range(len(nums)):
            for key_index in key_indices:
                if abs(i - key_index) <= k:
                    answer.append(i)
                    break
        return sorted(set(answer))
    
    
        
        
        