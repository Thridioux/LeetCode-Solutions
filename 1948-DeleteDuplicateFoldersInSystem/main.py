from collections import defaultdict
from pyparsing import List

class Node:
    def __init__(self):
        self.children = {} # key: node string, value: Node
        self.deleted = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        def dfs(cur, path):
            if path and not cur.deleted:
                ans.append(path)
            if cur.deleted:
                return
            for k, v in cur.children.items():
                dfs(v, path + [k])
        
        def serialize(cur):
            if not cur.children:
                return ""
            ans = ""
            for k in sorted(cur.children.keys()):
                ans += k + "(" + serialize(cur.children[k]) + ")"
            trees[ans].append(cur)
            return ans
            
        # insert a path into the trie
        def insert(path):
            cur = root
            for c in path:
                if c not in cur.children:
                    cur.children[c] = Node()
                cur = cur.children[c]

        root = Node()
        trees = defaultdict(list) # key; serialized subtree string, value: root node of that subtree
        
        #build the trie
        for path in paths:
            insert(path)
            
        #serialize all the subtrees
        serialize(root)

        # mark all the subtrees who has the same structure
        for nodes in trees.values():        
            if len(nodes) > 1:
                for node in nodes:
                    node.deleted = True
                    
        ans = []
        #traverse the tree to get the remaining folders
        dfs(root, [])
        
        return ans 
            