# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Example 1:

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 
# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 or l2:
            if l1:
                x = l1.val
            else:
                x = 0
            if l2:
                y = l2.val
            else:
                y = 0
            sum = x + y + carry
            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            current.next = ListNode(carry)
        return dummy.next

# ll1 = ListNode(2)
# ll1.next = ListNode(4)
# ll1.next.next = ListNode(3)

# ll2 = ListNode(5)
# ll2.next = ListNode(6)
# ll2.next.next = ListNode(4)

# s = Solution()
# result = s.addTwoNumbers(ll1, ll2)
# while result:
#     print(result.val)
#     result = result.next
# # Output: 7 0 8
    
ll1 = ListNode(0)
ll2 = ListNode(0)

s = Solution()
result = s.addTwoNumbers(ll1, ll2)

result = s.addTwoNumbers(ll1, ll2)
s.addTwoNumbers(ll1, ll2)


while result:
    print(result.val)
    result = result.next

# Output: 0


ll1 = ListNode(9)


