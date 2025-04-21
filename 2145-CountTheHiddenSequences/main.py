class Solution:
    def numberOfArrays(self, differences, lower, upper) :
        current_sum = 0
        min_sum = 0
        max_sum = 0
        for diff in differences:
            current_sum += diff
            min_sum = min(min_sum, current_sum)
            max_sum = max(max_sum, current_sum)
            
    
        sequence_range = max_sum - min_sum
        allowed_range = upper - lower 
        
        if sequence_range > allowed_range:
            return 0
        
        return allowed_range - sequence_range + 1