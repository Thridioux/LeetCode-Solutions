from collections import defaultdict

class Solution(object):
    def treeQueries(self, root, queries):
        heights = {}
        depth_map = {}
        max_height_at_depth = defaultdict(list)

        # DFS to calculate heights and assign nodes to depths
        def dfs(node, depth):
            if not node:
                return 0
            left_height = dfs(node.left, depth + 1)
            right_height = dfs(node.right, depth + 1)
            h = 1 + max(left_height, right_height)
            heights[node.val] = h
            depth_map[node.val] = depth
            max_height_at_depth[depth].append(h)
            return h

        # Initial DFS to populate `heights`, `depth_map`, and `max_height_at_depth`
        dfs(root, 0)

        # Precompute only the top two heights for each depth level
        for depth, height_list in max_height_at_depth.items():
            height_list.sort(reverse=True)  # Sort heights in descending order
            if len(height_list) > 2:
                max_height_at_depth[depth] = height_list[:2]  # Keep only top two heights

        results = []
        for q in queries:
            depth_q = depth_map[q]
            height_q = heights[q]

            if len(max_height_at_depth[depth_q]) == 1:
                # Only one node at this depth; removing it removes the contribution
                new_height = depth_q - 1
            else:
                # More than one node at this depth
                if max_height_at_depth[depth_q][0] == height_q:
                    # The queried node is the tallest, use the second tallest
                    new_height = depth_q + max_height_at_depth[depth_q][1] - 1
                else:
                    # Queried node is not the tallest, use the tallest
                    new_height = depth_q + max_height_at_depth[depth_q][0] - 1

            results.append(new_height)

        return results
