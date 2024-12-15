import heapq

class Solution:
    def maxAverageRatio(self, classes, extraStudents):
        # Helper function to calculate the gain of adding one student
        def gain(p, t):
            return (p + 1) / (t + 1) - p / t

        # Max heap to store classes by their potential gain
        heap = []
        for p, t in classes:
            heapq.heappush(heap, (-gain(p, t), p, t))  # Store negative gain to simulate max heap

        # Distribute extra students
        while extraStudents > 0:
            _, p, t = heapq.heappop(heap)
            # Add one extra student to the class
            p += 1
            t += 1
            # Push the updated class back into the heap
            heapq.heappush(heap, (-gain(p, t), p, t))
            extraStudents -= 1

        # Calculate the final average pass ratio
        total_ratio = sum(p / t for _, p, t in heap)
        return total_ratio / len(classes)

    
#test cases
classes = [[2,4],[3,9],[4,5],[2,10]]
extraStudents = 4
solution = Solution()
print(solution.maxAverageRatio(classes, extraStudents))  # Expected: 0.78333
