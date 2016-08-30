# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
            
        hare = tort = head
        
        while tort and hare and hare.next:
            tort = tort.next
            hare = hare.next.next
            if tort is hare:
                return True
            
        return False
