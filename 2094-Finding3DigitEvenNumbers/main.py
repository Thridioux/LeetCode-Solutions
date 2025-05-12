class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.sort()
        result = []
        for i in range(len(digits)):
            if digits[i] == 0:
                continue
            for j in range(len(digits)):
                if i == j:
                    continue
                for k in range(len(digits)):
                    if i == k or j == k:
                        continue
                    if digits[k] % 2 == 0:
                        result.append(digits[i] * 100 + digits[j] * 10 + digits[k])
        return sorted(list(set(result)))