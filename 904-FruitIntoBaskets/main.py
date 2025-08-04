from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        max_fruits = 0
        fruit_count = {}
        
        for right in range(len(fruits)):
            fruit_count[fruits[right]] = fruit_count.get(fruits[right], 0) + 1 # Count the fruit at the right pointer
            
            while len(fruit_count) > 2:  # More than 2 types of fruits
                fruit_count[fruits[left]] -= 1  # Remove the fruit at the left
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left += 1  # Move the left pointer to the right

            max_fruits = max(max_fruits, right - left + 1)
            
        return max_fruits
    



        