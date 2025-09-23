from typing import List
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split the version strings by '.'
        v1_parts = version1.split('.')
        v2_parts = version2.split('.')
        
        # Convert parts to integers to ignore leading zeros
        v1_nums = [int(part) for part in v1_parts]
        v2_nums = [int(part) for part in v2_parts]
        
        # Compare each part
        max_length = max(len(v1_nums), len(v2_nums))
        for i in range(max_length):
            num1 = v1_nums[i] if i < len(v1_nums) else 0
            num2 = v2_nums[i] if i < len(v2_nums) else 0
            
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
        
        return 0
        