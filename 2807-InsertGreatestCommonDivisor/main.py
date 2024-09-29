
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #find the greatest common divisor between two nodes in linked list
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        cur = head
        while cur.next:
            n1, n2 = cur.val, cur.next.val
            cur.next = ListNode(gcd(n1, n2), cur.next)
            cur = cur.next.next
        return head
            
        