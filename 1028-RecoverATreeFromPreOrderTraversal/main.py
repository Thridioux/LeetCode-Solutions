# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str):
        dashes = 0 #depth
        stack = []
        i = 0
        while i < len(traversal):
            if traversal[i] == '-':
                dashes += 1
                i += 1
            else:
                j = i
                while j < len(traversal) and traversal[j] != '-':
                    j += 1
                    
                val = int(traversal[i:j])
                node = TreeNode(val)
                
                while len(stack) > dashes:
                    stack.pop()
                    
                if stack and not stack[-1].left:
                    stack[-1].left = node
                elif stack:
                    stack[-1].right = node
                stack.append(node)
                dashes = 0
                i = j
        return stack[0]
                