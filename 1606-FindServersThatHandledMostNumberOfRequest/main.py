import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        counts = [0] * k
        busy = []  # min-heap storing (finish_time, server_id)
        
        # available stores "virtual server indices".
        # For request i, the preferred server index is i.
        # Any server 'sid' is represented by the smallest integer >= i where v % k == sid,
        # which is exactly: i + (sid - i) % k.
        # This preserves the wrap-around cyclic order without needing an explicit balanced BST.
        available = list(range(k))
        heapq.heapify(available)
        
        for i, (arr, ld) in enumerate(zip(arrival, load)):
            # Free up all servers that have finished handling their requests by time `arr`
            while busy and busy[0][0] <= arr:
                _, sid = heapq.heappop(busy)
                heapq.heappush(available, i + (sid - i) % k)
                
            # If no servers are available, the request is dropped
            if not available:
                continue
                
            # Pick the server closest to (i % k) in circular order
            chosen_v = heapq.heappop(available)
            chosen = chosen_v % k
            counts[chosen] += 1
            heapq.heappush(busy, (arr + ld, chosen))
            
        max_requests = max(counts)
        return [idx for idx, c in enumerate(counts) if c == max_requests]
