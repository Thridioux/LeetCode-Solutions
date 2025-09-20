from collections import defaultdict, deque
from typing import List
import bisect
class Router:

    def __init__(self, memoryLimit: int):
        self.size = memoryLimit
        self.packets = {} # key ->[source, destination, timestamp]
        self.counts = defaultdict(list) # destination -> count
        self.queue = deque() # FIFO order of packets
        

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = self._encode(source, destination, timestamp)
        
        # duplicate check 
        if key in self.packets:
            return False
        
        #if memory full, forward oldest packet
        if len(self.packets) >= self.size:
            self.forwardPacket()
        
        # add packet
        self.packets[key] = [source, destination, timestamp]
        self.queue.append(key)
        self.counts[destination].append(timestamp)
        return True
            
        
    def forwardPacket(self) -> List[int]:
        if not self.packets:
            return []

        key = self.queue.popleft()
        packet = self.packets.pop(key)
        
        dest = packet[1]
        self.counts[dest].pop(0) # remove the oldest timestamp for this destination
        
        return packet
        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.counts.get(destination, [])
        if not timestamps:
            return 0
        
        #binary search for the range
        left = bisect.bisect_left(timestamps, startTime)
        right = bisect.bisect_right(timestamps, endTime)
        
        return right - left
    
    def _encode(self, source: int, destination: int, timestamp: int) -> int:
        #encode uniquely into 1 number 
        return (source << 40) | (destination << 20) | timestamp
        
        
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)