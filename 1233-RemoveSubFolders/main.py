class Trie:
    def __init__(self):
        self.children = {}
        self.end_of_folder = False
        
    def add(self, path):
        cur = self
        for f in path.split('/'):
            if f not in cur.children:
                cur.children[f] = Trie()
            cur = cur.children[f]
        cur.end_of_folder = True  # Mark this as a complete folder path
    
    def prefix_search(self, path):
        cur = self
        folders = path.split('/')
        for f in folders:
            if f in cur.children:
                cur = cur.children[f]
                if cur.end_of_folder:
                    return True  # Found a prefix folder, indicating a subfolder
            else:
                return False  # No prefix exists for this path
        return False  # Path is unique, no prefix folder found

    
class Solution:
    def removeSubfolders(self, folder):
        # Sort folders by length to ensure roots are added before subfolders
        folder.sort(key=len)
        
        trie = Trie()
        res = []
        for f in folder:
            if not trie.prefix_search(f):  # Only add if no prefix (parent) folder exists
                res.append(f)
                trie.add(f)  # Add the root folder to the Trie to mark it for future subfolder checks
        
        return res
