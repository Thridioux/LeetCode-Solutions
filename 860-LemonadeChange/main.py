class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        count = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            count[bill] += 1
            if bill == 10:
                if count[5] > 0:
                    count[5] -= 1
                else:
                    return False
            elif bill == 20:
                if count[10] > 0 and count[5] > 0:
                    count[10] -= 1
                    count[5] -= 1
                elif count[5] >= 3:
                    count[5] -= 3
                else:
                    return False
        return True

# Test cases
bills = [5, 10, 20]
# Expected: False, because after receiving a $10 bill, there is no $5 bill left for change
print(Solution().lemonadeChange(bills))
