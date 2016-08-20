tion for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dum = ListNode(-1)
        dum.next = head
        prev = dum
        while head != None:
            
            if head.val == val:
                prev.next = head.next
                head = None
            else:
                prev = head
            
            head = prev.next
            
        return dum.next
