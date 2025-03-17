class Solution:
    def divideArray(self, nums) -> bool:
        odd_set = set()
        
        for n in nums:
            if n not in odd_set:
                odd_set.add(n)
            else:
                odd_set.remove(n)
        
        return len(odd_set) == 0
    
    
# class Solution:
#     def divideArray(self, nums) -> bool:
#         count = {}
        
#         for n in nums:
#             if n not in count:
#                 count[n] = 0
#             count[n] += 1
        
#         for n, cnt in count.items():
#             if cnt % 2 ==1:
#                 return False
#         return True
        