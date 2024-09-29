# class Solution(object):
#     def twoSum(self,nums,target):
#         self.nums = nums
#         self.target = target
#         for i in range(len(self.nums)):
#             for j in range(i+1,len(self.nums)):
#                 if self.nums[i] + self.nums[j] == self.target:
#                     return [i,j]
#         return None # if no solution found
    
# # test the result
# s = Solution()
# result = s.twoSum([2,7,11,15],9)
# print(result)
                


class Solution:
    def twoSum(self, list, target):
        for i in list: # for each element in the list
            m=list[list.index(i)+1:] # create a sublist starting from the next element of the current element
            if target-i in m: # if the difference between the target and the current element is in the sublist
                return [list.index(i),m.index((target-i))+len(list)-len(m)]
            
# test the result   

s = Solution()
result = s.twoSum([2,7,11,15],9)
print(result)           
        

    
        
                