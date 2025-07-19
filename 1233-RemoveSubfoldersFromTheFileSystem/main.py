from typing import List

class Trie:
    def __init__(self):
        self.children = {} # string -> Trie
        self.is_end = False
        
    def add(self, path):
        cur = self
        for f in path.split('/'):
            if f not in cur.children:
                cur.children[f] = Trie()
            cur = cur.children[f]
        cur.is_end = True
            
        
    def prefix_search(self, path):
        cur = self
        folders = path.split('/')
        for i in range(len(folders) - 1):
            cur = cur.children[folders[i]]
            if cur.is_end:
                return True
        
    
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for path in folder:
            trie.add(path)
        
        result = []
        for path in folder:
            if not trie.prefix_search(path):
                result.append(path)
        
        return result
    
    
            
        
        