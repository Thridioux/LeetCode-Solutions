class Solution:
    def threeConsecutiveOdds(self, arr):
        #return True if there are three consecutive odd numbers in the array
        for i in range(len(arr) - 2):
            if arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2] % 2 == 1:
                return True
        return False

        