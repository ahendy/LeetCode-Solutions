# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # find middle while pushing to a stack
        # pop and iterate from mid
        # even odd?
        if not head:
            return True
        
        pre = fast = slow = head
        
        
        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        
        
        if fast:
            slow = slow.next
        mid = slow
        pre.next = None
        # reverse head
        
        pre = None
        while head:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
        
        
        head = pre
        
        while head and slow:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next
        
        return True
            
        
        
        
        
        
