class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        candidates.sort()
        result = []
        self.backtrack(candidates, target, 0, [], result)
        return result
    
    def backtrack(self, candidates, target, start, path, result):
        if target == 0:
            result.append(path)
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            self.backtrack(candidates, target-candidates[i], i+1, path+[candidates[i]], result)

# Test Cases
candidates = [10,1,2,7,6,1,5]
target = 8
solution = Solution()
print(solution.combinationSum2(candidates, target))  # Expected output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]