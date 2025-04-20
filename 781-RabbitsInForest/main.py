class Solution:
    def numRabbits(self, answers) -> int:
        from collections import Counter
        counts = Counter(answers)
        total_rabbits = 0
        
        for x,count in counts.items():
            # Calculate the number of rabbits based on the formula
            # (count + x) // (x + 1) gives the number of groups needed
            # Each group has x + 1 rabbits
            group_size = (x + 1)
            num_groups = (count + x) // group_size
            total_rabbits += num_groups * group_size
            
        return total_rabbits