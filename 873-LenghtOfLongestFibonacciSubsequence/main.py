class Solution:
    def lenLongestFibSubseq(self, arr):
        arr_set = set(arr)
        res = 0
        #brute force 
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                prev, curr = arr[i], arr[j]
                nxt = prev + curr
                length = 2
                while nxt in arr_set:
                    length += 1
                    prev, curr = curr, nxt
                    nxt = prev + curr
                    res = max(res, length)
        return res if res > 2 else 0

        