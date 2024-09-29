from collections import Counter
import heapq
class AllOne(object):

    def __init__(self):
        self.d = Counter()
        self.maxheap = []
        self.minheap = []

    def inc(self, key):
        """
        :type key: str
        :rtype: None
        """
        self.d[key] += 1
        heapq.heappush(self.maxheap, (-self.d[key], key))
        heapq.heappush(self.minheap, (self.d[key], key))
        

    def dec(self, key):
        """
        :type key: str
        :rtype: None
        """
        if key in self.d:
            self.d[key] -= 1
            if self.d[key] == 0:
                del self.d[key]
            else:
                heapq.heappush(self.maxheap, (-self.d[key], key))
                heapq.heappush(self.minheap, (self.d[key], key))
         

    def getMaxKey(self):
        """
        :rtype: str
        """
        while self.maxheap:
            count, key = self.maxheap[0]
            if -count == self.d[key]:
                return key
            heapq.heappop(self.maxheap)
            
        return ""

    def getMinKey(self):
        """
        :rtype: str
        """
        while self.minheap:
            count, key = self.minheap[0]
            if count == self.d[key]:
                return key
            heapq.heappop(self.minheap)
            
        return ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()