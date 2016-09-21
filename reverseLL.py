
class Node():

	def __init__(self, val):
		self.val = val
		self.next = None

def iterator(head):
	
	while head is not None:
		yield head.val
		head = head.next

def reverse_LL(head):
	
	prev = None

	while head is not None:
		next = head.next
		head.next = prev
		prev = head
		head = next

	return prev

def reverse_LL_recurse(head, prev=None):

	next = head.next
	head.next = prev
	return head if next is None else reverse_LL_recurse(next, head)


if __name__=='__main__':
	n1 = Node(1)
	n2 = Node(2)
	n3 = Node(3)
	n4 = Node(4)
	n1.next = n2
	n2.next = n3
	n3.next = n4

	l1 = [i for i in iterator(n1)]
	assert l1 == [1,2,3,4]

	reverse = reverse_LL(n1)
	reverse_l1 = iterator(reverse)
	assert [4,3,2,1] == list(reverse_l1)

	rev = reverse_LL_recurse(n4)
	assert list(iterator(rev)) == [1,2,3,4]
