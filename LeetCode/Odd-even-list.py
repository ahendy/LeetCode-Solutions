# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = o = None
        if head is None:
            return
        
        e = head
        if head.next:
            oddhead = o = head.next        
            curr = head.next.next
        else:
            return head
        
        while curr and curr.next:
            e.next = curr
            
            o.next = curr.next
            o = o.next

            curr = curr.next.next
            e = e.next
          
            
        if o.next:
            e.next = o.next
            e = e.next
            o.next = None
        e.next = oddhead
        
        return head
            
            
            
            
            
            
