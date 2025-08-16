class Solution:
    def maximum69Number (self, num: int) -> int:
        #convert the number in an array of its digits
        digits = [int(d) for d in str(num)]
        #find the first 6 and change it to 9
        for i in range(len(digits)):
            if digits[i] == 6:
                digits[i] = 9
                break
        #convert the array back to an integer
        return int(''.join(map(str, digits)))