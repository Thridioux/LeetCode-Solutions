class Solution:
    def divideString(self, s: str, k: int, fill: str):
        # Split the string into groups of size k and fill the last group if necessary
        n = len(s)
        result = []
        for i in range(0, n, k):
            group = s[i:i + k]
            if len(group) < k:
                group += fill * (k - len(group))
            result.append(group)
        return result
    
    
        
        