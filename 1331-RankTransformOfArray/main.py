class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # replace each element with its rank
        # the rank is an integer starting from 1
        # the larger the element, the larger the rank
        # if two elements are equal, their rank must be the same
        # return the ranks in an array
        
        sorted_arr = sorted(arr)
        rank = {}
        rank_count = 1
        for num in sorted_arr:
            if num not in rank:
                rank[num] = rank_count
                rank_count += 1
        return [rank[num] for num in arr]

# Time complexity: O(nlogn)
# Space complexity O(n)
#test cases
solution = Solution()
print(solution.arrayRankTransform([40,40,40,40])) #[4,1,2,3]