# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def spiralMatrix(self, m, n, head): # m rows, n columns
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        left, right = 0, n # right pointer is 1 position out of bounds
        top , bottom = 0, m # bottom pointer is 1 position out of bounds
        grid = [[-1] * n for _ in range(m)]
        
        while head:
            # 1.left to right
            for i in range(left, right):
                if not head: # if head is None, return res
                    return grid
                grid[top][i] = head.val
                head = head.next
            top += 1
            
            # 2.top to bottom
            for i in range(top, bottom):
                if not head: # if head is None, return grid
                    return grid
                grid[i][right-1] = head.val
                head = head.next
            right -= 1
            
            # 3.right to left
            for i in range(right-1, left-1, -1):
                if not head: # if head is None, return grid
                    return grid
                grid[bottom-1][i] = head.val
                head = head.next
            bottom -= 1
            
            # 4.bottom to top
            for i in range(bottom-1, top-1, -1):
                if not head: # if head is None, return grid
                    return grid
                grid[i][left] = head.val
                head = head.next
            left += 1
        return grid    
    
    
# Time complexity: O(m*n)
# Space complexity: O(m*n)
#test cases
def listToLinkedList(lst):
    dummy = ListNode()
    head = dummy
    for val in lst:
        head.next = ListNode(val)
        head = head.next
    return dummy.next

# Test case
m = 3
n = 5
head = listToLinkedList([3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0])
sol = Solution()
result = sol.spiralMatrix(m, n, head)
for row in result:
    print(row)