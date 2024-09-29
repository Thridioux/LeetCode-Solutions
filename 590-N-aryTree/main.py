"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        #recursive
        # res = []
        # def helper(node):
        #     if not node:
        #         return
        #     for child in node.children:
        #         helper(child)
        #     res.append(node.val)
        # helper(root)
        # return res
    
    #iterative
        if not root:
            return []
        res = []
        stack = [(root, False)]
        while stack:
            node , visited = stack.pop()
            if visited:
                res.append(node.val)
            else:
                stack.append((node, True))
                for child in node.children[::-1]:
                    stack.append((child, False))
        return res
'''
        1
       / \
      2   3
     / \   \
    4   5   6

'''   #[4, 5, 2, 6, 3, 1]

    
        
    

    
            