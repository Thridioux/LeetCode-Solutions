class Solution:
    def kthDistinct(self,arr,k):
        count = {}
        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        distinct = []
        for i in arr:
            if count[i] == 1:
                distinct.append(i)

        if k > len(distinct):
            return ''
        
        return distinct[k-1]
        
            
            
                    
# Example usage:
arr = ["d","b","c","b","c","a"]
k = 2
solution = Solution()
output = solution.kthDistinct(arr, k)
print(output)  # Output: 2






