class Solution:
    def minMaxDifference(self, num: int) -> int:
        #to achieve the max diff try to remap first non-nine digit to 9
        num_str = str(num)
        max_num = num_str
        for i in range(len(num_str)):
            if num_str[i] != '9':
                max_num = num_str.replace(num_str[i], '9')
                break
        #to achieve the min diff try to remap first non-zero digit to 0
        min_num = num_str
        for i in range(len(num_str)):
            if num_str[i] != '0':
                min_num = num_str.replace(num_str[i], '0')
                break
        return int(max_num) - int(min_num)
        
        