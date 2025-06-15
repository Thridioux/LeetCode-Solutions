class Solution:
    def maxDiff(self, num: int) -> int:
        s_num = str(num)
        
        a = s_num
        for digit in s_num:
            if digit != '9':
                a = s_num.replace(digit, '9')
                break
        
        b = s_num
        #case:1 change the first digit to '1'
        if s_num[0] != '1':
            b = s_num.replace(s_num[0], '1')
        else:
            #case:2 first digit is '1', find next digit to change to '0'
            for digit in s_num[1:]:
                if digit not in '01':
                    b = s_num.replace(digit, '0')
                    break
        
        return abs(int(a) - int(b))