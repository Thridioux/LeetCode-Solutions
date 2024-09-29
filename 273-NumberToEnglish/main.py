class Solution:
    def numberToEnglish(self,num):
        if num == 0:
            return "zero"
        elif num < 0:
            return "negative " + self.numberToEnglish(-num)
        elif num == 1000000000000:
            return "one trillion"
        else:
            return self.numberToEnglishHelper(num)
        
    def numberToEnglishHelper(self,num):
        if num == 0:
            return ""
        elif num < 20:
            return ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"][num-1]
        elif num < 100:
            return ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"][num//10-2] + (" " + self.numberToEnglishHelper(num%10) if num%10 != 0 else "")
        elif num < 1000:
            return self.numberToEnglishHelper(num//100) + " hundred" + (" " + self.numberToEnglishHelper(num%100) if num%100 != 0 else "")
        elif num < 1000000:
            return self.numberToEnglishHelper(num//1000) + " thousand" + (" " + self.numberToEnglishHelper(num%1000) if num%1000 != 0 else "")
        elif num < 1000000000:
            return self.numberToEnglishHelper(num//1000000) + " million" + (" " + self.numberToEnglishHelper(num%1000000) if num%1000000 != 0 else "")
        else:
            return self.numberToEnglishHelper(num//1000000000) + " billion" + (" " + self.numberToEnglishHelper(num%1000000000) if num%1000000000 != 0 else "")


test = Solution()
print(test.numberToEnglish(9999)) # one hundred twenty three million four hundred fifty six thousand seven hundred eighty nine