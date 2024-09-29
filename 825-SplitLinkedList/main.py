# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        #split the linked list into k parts
        #return the list of the k parts
        #if the linked list has n nodes, then the length of the parts should be as equal as possible
        #the parts should be in the order of the original linked list
        #parts occuring earlier should have a size greater than or equal to parts occuring later
        #return an array of k parts
        
        if not head:
            return [None]*k
        
        #count the number of nodes in the linked list
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        # determine the size of each part
        width, remainder = divmod(n, k) # n is the min number of nodes in each part, remainder is the number of parts that have n+1 nodes
        ans = []
        cur = head
        #split the linked list into k parts
        for i in range(k): #i is for the part index
            head = cur
            for j in range(width + (i < remainder) - 1): #j is for the part size
                if cur:
                    cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            ans.append(head)
        return ans

head = [1,2,3]
k = 5
print(Solution().splitListToParts(head, k))