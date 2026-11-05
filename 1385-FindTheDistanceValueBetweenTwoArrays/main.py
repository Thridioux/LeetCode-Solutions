class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        # Sort 'arr2' and use binary search to check if any element in 'arr2' is within distance 'd' of 'arr1[i]'.
        # Total time complexity: O(m log m + n log m), where n = len(arr1) and m = len(arr2).
        
        count = 0
        arr2.sort()
        for i in arr1:
            low = 0
            high = len(arr2) - 1
            while low <= high:
                mid = (low + high) // 2
                # If arr2[mid] is within distance d of i, i is invalid
                if abs(arr2[mid] - i) <= d:
                    break
                elif arr2[mid] < i:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                # No element in arr2 was within distance d of i
                count += 1
        return count
