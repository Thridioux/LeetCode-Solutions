class Solution:
    def tryRotationMatching(self, number: int, first, second) -> int:
        count = 0
        for i in range(len(first)):
            if first[i] == number:
                continue
            elif second[i] == number:
                count += 1
            else:
                return float('inf')
        return count

    def minDominoRotations(self, tops, bottoms) -> int:
        min_rotations = float('inf')
        for number in range(1, 7):
            count_tops = self.tryRotationMatching(number, tops, bottoms)
            count_bottoms = float('inf')
            if count_tops != float('inf'):
                count_bottoms = self.tryRotationMatching(number, bottoms, tops)
            min_rotations = min(min_rotations, count_tops, count_bottoms)
        return min_rotations if min_rotations != float('inf') else -1
