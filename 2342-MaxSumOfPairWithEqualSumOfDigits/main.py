class Solution:
    def maximumSum(self, nums):
        
        #find the sum of digits for each of the number in the list and store it in a dictionary
        
        sum_dict = {}
        for num in nums:
            digit_sum = sum(int(x) for x in str(num))
            if digit_sum not in sum_dict:
                sum_dict[digit_sum] = []
            sum_dict[digit_sum].append(num)
            
        no_pair = True 
        for key in sum_dict:
            if len(sum_dict[key]) > 1:
                no_pair = False
                break

        if no_pair:
            return -1
            
        # return the maximum sum of the pair with equal sum of digits
        max_sum = 0
        for key in sum_dict:
            if len(sum_dict[key]) > 1:
                sum_dict[key].sort()
                max_sum = max(max_sum, sum_dict[key][-1] + sum_dict[key][-2])
                
        return max_sum
        
        
    
    
        