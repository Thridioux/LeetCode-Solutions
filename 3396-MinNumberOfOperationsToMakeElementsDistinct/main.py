class Solution:
    def minimumOperations(self, nums):
        #remove first 3 elements until array is distinct and return the number of operations
        # check if the array is distinct
        def is_distinct(arr):
            return len(arr) == len(set(arr))
        
        # remove first 3 elements until array is distinct
        def remove_first_3(arr):
            return arr[3:] if len(arr) > 3 else []
        
        # count the number of operations
        def count_operations(arr):
            count = 0
            while not is_distinct(arr):
                arr = remove_first_3(arr)
                count += 1
            return count
        
        return count_operations(nums)
    
        
        