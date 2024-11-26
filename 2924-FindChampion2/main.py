class Solution(object):
    def findChampion(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        incoming = [0] * n
        
        for src,dst in edges:
            incoming[dst] += 1
            
        champions =[]
        for i,incoming_cnt in enumerate(incoming):
            if incoming_cnt == 0:
                champions.append(i)
                
        if len(champions) >1:
            return -1
        
        return champions[0]