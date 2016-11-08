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
        
        stack = []
        fast = slow = head

        while fast and fast.next:
            stack.append(slow)
            fast = fast.next.next
            slow = slow.next
        
        if fast:
            slow = slow.next
            
        while slow:
            top = stack.pop()
            if slow.val != top.val:
                return False
        
            slow = slow.next
            
        
        return True
            
