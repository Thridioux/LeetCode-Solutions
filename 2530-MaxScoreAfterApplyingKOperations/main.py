import heapq
import math

class Solution(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Step 1: Convert nums into a max-heap by negating the elements
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)  # Heapify the negated list
        
        score = 0
        
        # Step 2: Perform k operations
        for _ in range(k):
            # Step 3: Get the largest element (remember it's negated)
            largest = -heapq.heappop(max_heap)
            score += largest  # Add the largest value to the score
            
            # Step 4: Calculate ceil(largest / 3) and convert it to integer
            new_value = int(math.ceil(largest / 3.0))
            heapq.heappush(max_heap, -new_value)  # Push the negated new value into the heap
        
        return score

#test cases 
nums =[1,10,3,3,3] 
k = 3
print(Solution().maxKelements(nums, k)) # 15