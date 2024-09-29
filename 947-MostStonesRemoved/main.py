class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        parents = {}
        
        def find(x): # find the group which x belongs to , this function is used to find the root of the group .Root is representative of the group
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            parents.setdefault(x, x) # if x is not in the parents, set x as the parent of x
            parents.setdefault(y, y) 
            
            r1, r2 = find(x), find(y) 
            
            if r1 != r2:
                parents[r1] = r2
                
        for i,j in stones:
            union(i, ~j)
            
        roots = set()
        for key in parents:
            root = find(key)
            roots.add(root)
            
        return len(stones) - len(roots)

#test case 
stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
sol = Solution()
print(sol.removeStones(stones)) #5