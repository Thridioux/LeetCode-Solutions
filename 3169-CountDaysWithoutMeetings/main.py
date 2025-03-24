class Solution:
    def countDays(self, days: int, meetings):
        meetings.sort()
        prev_end = 0
         
        for start,end in meetings:
            start = max(start, prev_end+1)
            lenght = end - start + 1
            days -= max(0, lenght)
            prev_end = max(prev_end, end)
        
        return days
        