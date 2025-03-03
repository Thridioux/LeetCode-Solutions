class Solution:
    def pivotArray(self, nums,pivot):
        less = []
        pivotList = []
        greater = []
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                pivotList.append(num)
            else:
                greater.append(num)
        return less + pivotList + greater

        