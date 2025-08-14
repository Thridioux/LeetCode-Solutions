class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good_integer = ""
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                if num[i] > max_good_integer:
                    max_good_integer = num[i]
        return max_good_integer * 3 if max_good_integer else ""