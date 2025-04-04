# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root):
        def dfs(node):
            if not node:
                return (None, 0)

            left_node, left_height = dfs(node.left)
            right_node, right_height = dfs(node.right)
            
            if left_height == right_height:
                return node, 1+left_height 
            elif left_height > right_height:
                return left_node, 1+left_height
            else:
                return right_node, 1+right_height
            
        node, _ = dfs(root)
        return node