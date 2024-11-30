class Solution(object):
    def validArrangement(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict, deque
        graph = defaultdict(deque)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        
        for start, end in pairs:
            graph[start].append(end)
            in_degree[end] += 1
            out_degree[start] += 1
            
        
        #Find the start node
        start_node = pairs[0][0]
        for node in graph:
            if out_degree[node] > in_degree[node]:
                start_node = node
                break
            
        # Hierholzer's algorithm to find the euler path
        
        stack = [start_node]
        result = []
        
        while stack:
            while graph[stack[-1]]:
                next_node = graph[stack[-1]].popleft()
                stack.append(next_node)
            result.append(stack.pop())
            
        # format the result
        
        result = result[::-1]
        return [[result[i], result[i+1]] for i in range(len(result)-1)]