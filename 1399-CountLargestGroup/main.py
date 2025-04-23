class Solution:
    from collections import defaultdict
    def digit_sum(self, num):
        s = 0 
        while num > 0:
            s += num % 10
            num //= 10
        return s
    
    def countLargestGroup(self, n: int) -> int:
        from collections import defaultdict
        counts = defaultdict(int)
        max_size = 0
        
        for i in range(1, n + 1):
            d_sum = self.digit_sum(i)
            counts[d_sum] += 1
            max_size = max(max_size, counts[d_sum])
            
        result_count = 0
        for size in counts.values():
            if size == max_size:
                result_count += 1
        return result_count
        