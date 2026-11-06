from collections import defaultdict
from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs chronologically by request time
        logs.sort(key=lambda log: log[1])
            
        # Sort queries by time while preserving original indices
        sorted_queries = sorted(enumerate(queries), key=lambda item: item[1])
        
        server_counts = defaultdict(int)
        active_servers = 0
        ans = [0] * len(queries)
        
        left = 0
        right = 0
        m = len(logs)
        
        # Sliding window over logs for each query interval [q - x, q]
        for orig_idx, q in sorted_queries:
            # Expand window to include all logs up to time q
            while right < m and logs[right][1] <= q:
                server = logs[right][0]
                if server_counts[server] == 0:
                    active_servers += 1
                server_counts[server] += 1
                right += 1
            
            # Shrink window to remove all logs before time q - x
            while left < m and logs[left][1] < q - x:
                server = logs[left][0]
                server_counts[server] -= 1
                if server_counts[server] == 0:
                    active_servers -= 1
                left += 1
            
            # Number of servers that received zero requests in this window
            ans[orig_idx] = n - active_servers
            
        return ans