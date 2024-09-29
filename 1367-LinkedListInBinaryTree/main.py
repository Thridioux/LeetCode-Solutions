# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        #subtree of another tree
        def helper(list_node, tree_node):
            if not list_node: #if list is empty, return True
                return True
            if not tree_node or (list_node.val != tree_node.val) : #if tree is empty, return False
                return False
            
            return (
                helper(list_node.next , tree_node.left) or 
                helper(list_node.next , tree_node.right)
                    )
            
        if helper(head, root):
            return True
        if not root:   
            return False
        
        return (
            self.isSubPath(head, root.left) or 
            self.isSubPath(head, root.right)
        )    
        
            