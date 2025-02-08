from sortedcontainers import SortedList
from collections import defaultdict
class NumberContainers:

    def __init__(self):
        self.boxes = {}
        self.number_lookup = defaultdict(lambda: SortedList())
        

    def change(self, index: int, number: int) :
        if index in self.boxes:
            prev = self.boxes[index]
            self.number_lookup[prev].remove(index)
        
        self.boxes[index] = number
        self.number_lookup[number].add(index)
        

    def find(self, number: int) :
        if len(self.number_lookup[number]) == 0:
            return -1
        return self.number_lookup[number][0]
        

