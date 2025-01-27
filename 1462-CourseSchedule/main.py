class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        from collections import defaultdict
        adj = defaultdict(list)
        
        #every course is gonna be mapped to a list of prerequisites
        for prereq, crs in prerequisites:
            adj[crs].append(prereq)
        
        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for prereq in adj[crs]:
                    prereqMap[crs] = prereqMap[crs] | dfs(prereq) #union of hashsets
                prereqMap[crs].add(crs)
            return prereqMap[crs]
        

        prereqMap = {} #map crs --> hashset of indirect prereqs
        for crs in range(numCourses):
            dfs(crs)
            
        res = []
        for u,v in queries:
            res.append(u in prereqMap[v])
        return res