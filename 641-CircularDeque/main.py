class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.deque = []
        self.size = k
        
        

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.deque) < self.size:
            self.deque = [value] + self.deque
            return True
        else:
            return False
        
    
        

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.deque) < self.size:
            self.deque.append(value)
            return True
        else:
            return False
        

    def deleteFront(self):
        """
        :rtype: bool
        """
        if len(self.deque) > 0:
            self.deque.pop(0)
            return True
        else:
            return False
        

    def deleteLast(self):
        """
        :rtype: bool
        """
        if len(self.deque) > 0:
            self.deque.pop()
            return True
        else:
            return False
        

    def getFront(self):
        """
        :rtype: int
        """
        if len(self.deque) > 0:
            return self.deque[0]
        else:
            return -1
        
        

    def getRear(self):
        """
        :rtype: int
        """
        if len(self.deque) > 0:
            return self.deque[-1]
        else:
            return -1
        
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return len(self.deque) == 0
        

    def isFull(self):
        """
        :rtype: bool
        """
        return len(self.deque) == self.size
        
    
            

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

obj = MyCircularDeque(3)
obj.insertFront(1)
obj.insertFront(2)
obj.insertLast(3)
print(obj.getFront())
obj.traverse()