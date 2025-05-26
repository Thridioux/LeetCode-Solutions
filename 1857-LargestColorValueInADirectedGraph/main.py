class Solution:
    def largestPathValue(self, colors: str, edges):
        from collections import defaultdict, deque
        n = len(colors)
        adj = defaultdict(list)
        in_degree = [0] * n
        
        for u_node, v_node in edges:
            adj[u_node].append(v_node)
            in_degree[v_node] += 1
            
        dp_counts = [[0] * 26 for _ in range(n)]
        
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)

        max_color_value = 0
        nodes_processed_count = 0
        max_color_value_found = 0
        
        while queue:
            u_node = queue.popleft()
            nodes_processed_count += 1
            
            #update counts for the u node's own color
            color_char_code_u = ord(colors[u_node]) - ord('a')
            dp_counts[u_node][color_char_code_u] += 1
            
            max_color_value_found = max(max_color_value_found,dp_counts[u_node][color_char_code_u])
            
            for v_node in adj[u_node]:
                #propogate all color counts from u_node to v_node
                for k_color_code in range(26):
                    dp_counts[v_node][k_color_code] = max(dp_counts[v_node][k_color_code], dp_counts[u_node][k_color_code]) 
                    
                in_degree[v_node] -= 1
                if in_degree[v_node] == 0:
                    queue.append(v_node)
                    
        if nodes_processed_count < n:
            return -1
        else:
            return max_color_value_found