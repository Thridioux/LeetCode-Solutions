class Solution:
    def findLucky(self, arr) -> int:
        # return the largest lucky number is an integer that has a frequency equal to its value
        # if no lucky number exists, return -1
        count = {}
        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        lucky_numbers = [num for num, freq in count.items() if num == freq]
        return max(lucky_numbers) if lucky_numbers else -1
        
        