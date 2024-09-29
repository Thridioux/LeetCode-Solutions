from collections import deque
class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        results = []
        deq = deque()
        for i in range(n):
            if deq and deq[0] < i - k + 1:
                deq.popleft()
            while deq and nums[deq[-1]] <= nums[i]:
                deq.pop()
            deq.append(i)

            if i >= k - 1:
                window = nums[i-k+1:i+1]
                if all(window[j]+1 == window[j+1] for j in range(k-1)):
                    results.append(nums[deq[0]])
                else:
                    results.append(-1)
        return results