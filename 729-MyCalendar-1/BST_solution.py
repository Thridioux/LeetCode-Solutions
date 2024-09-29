
class Tree:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        
    
    def insert(self, start, end):
        curr = self
        while True:
            if start >= curr.end:
                if not curr.right:
                    curr.right = Tree(start, end)
                    return True
                curr = curr.right
            elif end <= curr.start:
                if not curr.left:
                    curr.left = Tree(start, end)
                    return True
                curr = curr.left
            else:
                return False


class MyCalendar(object):

    def __init__(self):
        self.root = None
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.root:
            self.root = Tree(start, end)
            return True
        return self.root.insert(start, end)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)