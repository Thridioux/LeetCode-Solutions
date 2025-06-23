class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_palindrome(x: str)-> bool:
            return x == x[::-1]
        
        def to_base_k(x: int, k: int) -> str:
            if x == 0:
                return '0'
            digits = []
            while x > 0:
                digits.append(str(x % k))
                x //= k
            return ''.join(digits[::-1])
        
        count = 0
        total_sum = 0
        lenght = 1
        
        while count < n:
            #generate odd lenght palindrome 
            for i in range(10**(lenght - 1), 10**lenght):
                s = str(i)
                num_str = s + s[:-1][::-1]  # odd length palindrome
                num = int(num_str)
                base_k_str = to_base_k(num, k)
                if  is_palindrome(base_k_str):
                    count += 1
                    total_sum += num
                    if count == n: return total_sum
                    
            #generate even lenght palindrome
            for i in range(10**(lenght -1), 10**lenght):
                s = str(i)
                num_str = s + s[::-1]
                num = int(num_str)
                base_k_str = to_base_k(num, k)
                if is_palindrome(base_k_str):
                    count += 1 
                    total_sum += num
                    if count == n: return total_sum
            lenght += 1
            
        return total_sum
                    
            
                    
                    
                    
                
                        
                    
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            
                
                
            
            
        
        
        
        
        
        
        
        
        




        