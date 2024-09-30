class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.maxSize = maxSize
        self.stack = []
        self.size = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        #add x to the top of the stack if the stack has not reached its maximum size
        if self.size < self.maxSize:
            self.stack.append(x)
            self.size += 1
        

        

    def pop(self):
        """
        :rtype: int
        """
        #pop the top element of the stack if the stack is not empty return -1 otherwise
        if self.size > 0:
            self.size -= 1
            return self.stack.pop() 
        else:
            return -1
        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        #increment the first k elements of the stack by val if there are less than k elements in the stack increment all elements
        if self.size < k:
            for i in range(self.size):
                self.stack[i] += val
        else:
            for i in range(k):
                self.stack[i] += val
                
        
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)