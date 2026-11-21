from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        last_seen = {}
        prev_val = [None] * n
        new_parent = list(parent)
        order = []
        
        # Iterative DFS to find the closest ancestor with the same character
        stack = [(0, False)]
        while stack:
            u, is_backtracking = stack.pop()
            c = s[u]
            if is_backtracking:
                last_seen[c] = prev_val[u]
            else:
                order.append(u)
                if u != 0 and c in last_seen and last_seen[c] is not None:
                    new_parent[u] = last_seen[c]
                prev_val[u] = last_seen.get(c, None)
                last_seen[c] = u
                stack.append((u, True))
                for v in adj[u]:
                    stack.append((v, False))
                    
        # Compute subtree sizes in the new tree
        # Since every new parent is an ancestor in the original tree,
        # processing nodes in reverse pre-order guarantees a valid topological order.
        ans = [1] * n
        for u in reversed(order):
            p = new_parent[u]
            if p != -1:
                ans[p] += ans[u]
                
        return ans