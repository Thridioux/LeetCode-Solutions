class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(num))  # Convert the number to a list of digits
        n = len(num)
        
        # Track the last seen index of each digit (0 to 9)
        last = {int(x): i for i, x in enumerate(num)}
        
        # Traverse through the number
        for i in range(n):
            # Check if there's a larger digit later that can be swapped
            for d in range(9, int(num[i]), -1):
                if last.get(d, -1) > i:
                    # Swap the current digit with the larger digit found
                    num[i], num[last[d]] = num[last[d]], num[i]
                    # Return the swapped number as an integer
                    return int(''.join(num))
        
        # If no swap was made, return the original number
        return int(''.join(num))

# test cases
# 98368 -> 98863

num = 9973
sol = Solution()
print(sol.maximumSwap(num))
