class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        import heapq 
        indexes = [i for i in range(len(times))]
        indexes.sort(key = lambda i : times[i][0]) #sort by arrival time

        used_chairs = []   # (leave_time, chair)
        available_chairs =[i for i in range(len(times))] #(chair)

        for i in indexes:
            a,l  = times[i] # unpacked the number of times and the index
            while used_chairs and used_chairs[0][0]<= a:
                leave ,chair = heapq.heappop(used_chairs)
                heapq.heappush(available_chairs, chair)

            chair = heapq.heappop(available_chairs)
            heapq.heappush(used_chairs, (l, chair))
            
            if i == targetFriend:
                return chair
            
        
    
                
        


            




            



