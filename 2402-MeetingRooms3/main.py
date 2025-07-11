from typing import List
import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = [i for i in range(n)] # sorted array is actually a min-heap
        used = [] #(end_time, room_number)
        count = [0] * n # count[n] = meetings schedule 
        
        for start, end in meetings:
            # finish meetings 
            while used and start >= used[0][0]:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)
                
            # no room is avaliable
            if not available:
                end_time, room = heapq.heappop(used)
                end = end_time + (end - start)
                heapq.heappush(available, room)

            room = heapq.heappop(available)
            heapq.heappush(used, (end, room))
            count[room] += 1
            
                
        return count.index(max(count))
        
        
        