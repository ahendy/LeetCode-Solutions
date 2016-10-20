# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s = set()
        dumy = ListNode(-1)
        dumy.next = head
        
        prev = dumy
        while head:
            if head.val in s and prev:
                prev.next = head.next
                head = prev.next
            else:
                s.add(head.val)
                prev = head
                head = head.next
                
        return dumy.next
        
