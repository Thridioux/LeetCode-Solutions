class Solution:
    def maxScoreSightseeingPair(self, values):
        res = 0
        cur_max = values[0] - 1
        for i in range(1, len(values)):
            res = max(res, cur_max + values[i])
            cur_max = max(cur_max - 1, values[i] - 1)
        
        return res
        