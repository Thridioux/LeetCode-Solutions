class Solution:
    def maximumValueSum(self, nums, k, edges):
        ans = 0
        count = 0
        discarded_node = float('inf')  # Minimize the loss due to not finding XOR (Only applicable for ODD case)
        
        for num in nums:
            ans += max(num, num ^ k)
            count += 1 if (num ^ k) > num else 0
            discarded_node = min(discarded_node, abs(num - (num ^ k)))
        
        return ans if count % 2 == 0 else (ans - discarded_node)