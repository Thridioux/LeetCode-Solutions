class Solution:
    def countAndSay(self, n):
        if n == 1:
            return "1"
        
        current_result = "1"
        
        for _ in range(n-1):
            next_result = ""
            i = 0
            while i < len(current_result):
                count = 1
                current_digit = current_result[i]
                j = i + 1
                #count consecutive identical digits
                while j < len(current_result) and current_result[j] == current_digit:
                    count += 1
                    j += 1
                    
                #append the count and the digit to the next result
                next_result += str(count) + current_digit
                #move pointer i to the start of the next group
                i = j
            current_result = next_result
        return current_result
    
                

            
        