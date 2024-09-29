class MyCalendar(object):

    def __init__(self):
        self.events = [] # list of tuples (start, end)
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for s, e in self.events:
            if e > start and end > s:
                return False
        
        self.events.append((start, end))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

