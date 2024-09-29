class Solution:
    def countSeniors(self,details):
        ages= [int(s[11:13]) for s in details] 
        count=0
        for age in ages:
            if age>=60:
                count+=1
        return count
# test the solution
details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
sol = Solution()
print(sol.countSeniors(details)) # 2
