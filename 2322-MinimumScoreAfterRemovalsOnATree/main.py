from typing import List
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        xor_sum = [0] * n
        in_time = [0] * n
        out_time = [0] * n
        time = 0
        parent = [-1] * n
        
        # DFS to calculate xor_sum, in/out times, and parent
        def dfs(u, p):
            nonlocal time
            parent[u] = p
            in_time[u] = time
            time += 1
            xor_sum[u] = nums[u]
            for v in adj[u]:
                if v == p:
                    continue
                xor_sum[u] ^= dfs(v, u)
            out_time[u] = time
            time += 1
            return xor_sum[u]
        
        total_xor = dfs(0, -1)
        ans = float('inf')
        
        # Helper to check if u is ancestor of v
        def is_ancestor(u, v):
            return in_time[u] <= in_time[v] and out_time[v] <= out_time[u]
        
        # Collect all edges except the root's parent
        edge_nodes = []
        for i in range(1, n):
            edge_nodes.append(i)
        
        # Try all pairs of edges to cut
        for i in range(len(edge_nodes)):
            u = edge_nodes[i]
            for j in range(i+1, len(edge_nodes)):
                v = edge_nodes[j]
                # Check ancestor relationship
                if is_ancestor(u, v):
                    # v is in the subtree of u
                    part1 = xor_sum[v]
                    part2 = xor_sum[u] ^ xor_sum[v]
                    part3 = total_xor ^ xor_sum[u]
                elif is_ancestor(v, u):
                    # u is in the subtree of v
                    part1 = xor_sum[u]
                    part2 = xor_sum[v] ^ xor_sum[u]
                    part3 = total_xor ^ xor_sum[v]
                else:
                    # Disjoint subtrees
                    part1 = xor_sum[u]
                    part2 = xor_sum[v]
                    part3 = total_xor ^ xor_sum[u] ^ xor_sum[v]
                parts = sorted([part1, part2, part3])
                ans = min(ans, parts[2] - parts[0])
        return ans
