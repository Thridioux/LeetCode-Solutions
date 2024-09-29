import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """

        #min heap with kth largest integers
        self.min_heap = nums
        self.k = k

        #heapify the list
        heapq.heapify(self.min_heap)
        while len(self.min_heap) >k: #if the length of the heap is greater than k, pop the smallest element
            heapq.heappop(self.min_heap)



    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        #add the new value to the heap
        heapq.heappush(self.min_heap,val)
        if len(self.min_heap)>self.k:   
            heapq.heappop(self.min_heap)
       
        return self.min_heap[0]

# Your KthLargest object will be instantiated and called as such:

# obj = KthLargest(k, nums)   # 1,2,2,3,4
# param_1 = obj.add(val)

# Test Cases
k = 3
nums = [4,5,8,2]

kthLargest = KthLargest(k, nums)
print(kthLargest.add(3))  # Expected output: 4