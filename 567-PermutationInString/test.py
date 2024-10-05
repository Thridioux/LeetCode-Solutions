class Solution:
    def swap(self,s, i, j):
        s = list(s)
        s[i], s[j] = s[j], s[i]
        return ''.join(s)
    
    def permute(self,s,idx):
        #base case 
        if idx == len(s)-1:
            print(s)
            return

        for i in range(idx,len(s)):
            #swap
            s = self.swap(s,idx,i)
            #first element is fixed, permute the rest
            self.permute(s,idx+1)
            #backtrack
            s = self.swap(s,idx,i)
            
    def permuteString(self, s): #wrapper function
        self.permute(s,0)
            
            
        
    
    

