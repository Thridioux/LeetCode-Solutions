from typing import List
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # find the elements that have the max frequencies and count their total occurences
        
        freq = {}
        max_freq = 0
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            max_freq = max(max_freq, freq[num])
        
        # return the total count of elements with max frequency
        # if multiple elements have the same max frequency, count them all
        count = 0
        for count_freq in freq.values():
            if count_freq == max_freq:
                count += count_freq
        return count
    