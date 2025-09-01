from typing import List
import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
            #create a max heap storing (-gain, pass,total)
            max_heap = []
            for p,t in classes:
                if p == t:
                    # no gain possible if already 100%
                    heapq.heappush(max_heap, (0,p,t))
                else:
                    gain = (p+1)/(t+1) - p/t
                    heapq.heappush(max_heap, (-gain,p,t))
                    
            #distribute the extra students
            for _ in range(extraStudents):
                neg_gain, p, t = heapq.heappop(max_heap)
                p += 1
                t += 1
                if p == t:
                    new_neg_gain = 0
                else:
                    new_gain = (p+1)/(t+1) - p/t
                    new_neg_gain = -new_gain
                    
                heapq.heappush(max_heap, (new_neg_gain,p,t))
                
            #calculate the final average ratio
            total_ratio = 0
            for neg_gain, p, t in max_heap:
                total_ratio += p/t
                
            return total_ratio / len(classes)