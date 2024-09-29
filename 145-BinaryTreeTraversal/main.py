# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if not root : # if root is None
            return []
        stack = [root] # stack to store the nodes
        res = [] # list to store the values
        while stack:
            node = stack.pop()  
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]    
        
    
    
# Time complexity: O(n)
# Space complexity: O(n)

#test cases
root = [1,None,2,3]
Solution().postorderTraversal(root) # [3,2,1]
