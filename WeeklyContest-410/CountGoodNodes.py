from collections import defaultdict
class Solution(object):
    def countGoodNodes(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        tree = defaultdict(list) # Adjacency list 

        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        n = len(edges) + 1
        subtree_size = [0] * (n)
        
        def dfs(node, parent):
            size = 1
            for child in tree[node]:
                if child != parent:
                    size += dfs(child, node)
            subtree_size[node] = size
            return size
        

        dfs(0, -1) # Start from the root node 0 with no parent

        
        
        def is_good(node):
            child_sizes = set()
            for child in tree[node]:
                if subtree_size[child] != 0:
                    child_sizes.add(subtree_size[child])
            return len(child_sizes) <= 1
        
        good_nodes = 0

        def dfs_good(node, parent):
            nonlocal good_nodes
            if is_good(node):
                good_nodes += 1
            for child in tree[node]:
                if child != parent:
                    dfs_good(child, node)

        dfs_good(0, -1)    
        return good_nodes
       
    

# Test Case
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
solution = Solution()
print(solution.countGoodNodes(edges))  # Expected output: 7