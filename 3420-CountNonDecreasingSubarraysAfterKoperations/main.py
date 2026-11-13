from collections import deque
from typing import List


class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        r = n - 1
        cost = 0
        ans = 0
        # Monotonic deque of [val, count] representing contiguous blocks sharing
        # the same prefix maximum from l to r.
        q = deque()

        for l in range(n - 1, -1, -1):
            x = nums[l]
            cnt = 1
            while q and q[0][0] <= x:
                v, c = q.popleft()
                cost += (x - v) * c
                cnt += c
            q.appendleft([x, cnt])

            while cost > k:
                cost -= q[-1][0] - nums[r]
                q[-1][1] -= 1
                if q[-1][1] == 0:
                    q.pop()
                r -= 1

            ans += r - l + 1

        return ans
