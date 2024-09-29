class Solution(object):
    def countPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [str(num) for num in nums]
        count = 0

        def almost_equal(x, y):
            # If the numbers are already equal
            if x == y:
                return True
            
            # Case: One number is a single-digit and the other is a two-digit number
            if len(x) == 1 and len(y) == 2:
                # Check if swapping the digits of the two-digit number makes it equal to the single-digit number
                return x == y[0] or x == y[1]
            if len(x) == 2 and len(y) == 1:
                # Check if swapping the digits of the two-digit number makes it equal to the single-digit number
                return y == x[0] or y == x[1]
            
            # Ensure both numbers have the same length for valid swapping
            if len(x) != len(y):
                return False
            
            # Collect the indices where the digits differ
            mismatches = [(x[k], y[k]) for k in range(len(x)) if x[k] != y[k]]
            
            # To be almost equal, there must be exactly two mismatches
            # and swapping them should make the numbers equal
            return len(mismatches) == 2 and mismatches[0] == mismatches[1][::-1]

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if almost_equal(nums[i], nums[j]):
                    count += 1

        return count



test_cases = [
    ([3, 12, 30, 17, 21], 2),  # Test Case 1
    ([1, 1, 1, 1, 1], 10),  # Test Case 2
    ([123, 231], 0),  # Test Case 3
    ([123, 321], 0),  # Test Case 4
    ([12, 21, 34, 43], 2),  # Test Case 5
    ([12, 13, 21, 31, 32], 2),  # Test Case 6
    ([90, 9, 90, 90], 4),  # Test Case 7
    ([22, 22, 22, 33, 33], 4),  # Test Case 8
    ([11, 11, 22, 22, 33, 33, 44, 44], 6),  # Test Case 9
    ([56, 65, 56, 23, 32, 23], 4),  # Test Case 10
    ([70, 7, 70, 77, 7], 3),  # Test Case 11
    ([1, 10], 1),  # Test Case 12
    ([100, 10, 1], 2),  # Test Case 13
    ([0, 0, 0], 3),  # Test Case 14
    ([23, 32, 123, 321], 2),  # Test Case 15
    ([1234, 4321, 3412], 0),  # Test Case 16
    ([987, 789, 876], 0),  # Test Case 17
    ([55, 55, 555, 5], 3),  # Test Case 18
    ([999, 999], 1),  # Test Case 19
    ([88, 88, 88], 3),  # Test Case 20
]

# Running the tests
sol = Solution()
for idx, (nums, expected) in enumerate(test_cases):
    result = sol.countPairs(nums)
    print(f"Test Case {idx + 1}: Input: {nums} | Expected: {expected} | Got: {result}")
