# Coding_Challenges
Here's where I answer my daily Leetcode question. Below I will write a quick explanation for each of my answers. This repo will track as a place to track my problem solving ability as well as work on my algorithmic communication.

###[1. Two Sum ----(Easy)](https://leetcode.com/problems/two-sum/) 19:00 Monday, April 11 2016

Question uses hash maps, keeping track if the number that is required has been seen before. If it has, return the index pair. If it hasn't add it to the hash map. Straightforward enoough.

###[2. Add Two Numbers ----(Medium)](https://leetcode.com/problems/add-two-numbers) 20:00 Sunday, April 10 2016

Missed a few days (final exams, visiting home ), gotta catch up!

This problem is a cool one. Initiall it seems like it could be super simple but you realize that the carry from your sum could keep carrying. Because of this I initally came up with something like this which is recursive. Here's psuedocode.
		addtwo:
			while true
				if left pointer null
					head.next = addtwo right
				if right pointer null
					head.next = addtwo left
				val = l1 + l2 + carry
				head.next = node(val)


Here's how to compute the carry. First add the two numbers. Not sure if there is a faster way but this is what I made up. Divide by 10 to remove the ones place of your sum. Take the floor of this value. This will turn 7+8 = 15 to step 1: 15*0.1 = 1.5, step 2: floor(1.5) = 1 = carry. Now, the return value will be the the total sum aka (l1.val + l2.val + carry) - 10 * carry. 15-10 = 5 carry 1 -> [5, 1].

Now the algorithm begins by saving a front pointer to the linked list. I initiallize it with a zero, not sure if that's the best strategy (otherwise java will complain). The while loop makes sense because it should only stop once the list1 has gone through, list2 is complete and carry is not 0. Observe the case where list1 and list2 is null but there is still a carry leftover. We cant use null + null + carry so it must be cast to a 0. I do this through an if-then-else assignmment.
a = (condition? case true: case false). The rest is moving pointers forward if we need to.\

###[9. Palindrome Number ----(Easy)](https://leetcode.com/problems/palindrome-number/)
Just accepted a summer coop job, pretty happy!

Easy question, I was tired. A thing is a palidnrome if its reverse is equal to itself. In python you could use str(digit)[::-1] to reverse it but I wanted to do it with math rather than strings. To do this you build a number r by taking the mod 10 of the first number n, resulting in leftmost digit, next iteration multiplying r by 10 and dividing n by 10. I recommend writing this out in paper to visualize it first.

###[78. Subsets ----(Medium)](https://leetcode.com/problems/subsets/) 20:00 Sunday, April 3 2016

	
There are a couple ways to solve this. I use the fact that the sum of n choose i for i to n is equal to 2^n. This means that I can express each subset as a binary string where 1 means it is a part of the subset. Because converting an int (here is is value from 0 to 2^n) with bin() gives a binary string in the form 0b00001, I must slice the 0b and reverse it (although on second thought it will probably work if not reversed). This can be achieved using Python's list slicing tools [start:stop:step] with step value = -1 and stop = 1. Next it is a matter of iterating the string and if the value is a 1, add it to the current subset. The rest is straight forward!

###[104. Maximum Depth Tree ----(Easy)](https://leetcode.com/problems/maximum-depth-of-binary-tree/) 17:40 April 10

Standard tree traversal question. In this case each interation, save the number which you are at. If this is greater than the previous greatest depth, reassign the values. I do this in a bottom up fashion (postorder) as visiting the children of a tree will be a better depth than the parents.





###[136. Single Number ----(Medium](https://leetcode.com/problems/single-number/) 14:00 Tuesday, April 5


This problem looks like one I encountered in CSC225 with Bill Bird. It follows as: given a list integers 1 through n which has one missing, find the missing. Answer is linear time: expected sum = n(n-1)/2 from knowledge and then expected sum - real sum is answer. You follow the same principle with this problem, except, given is random integers not just 1..n. This means you have to use a hash table/bucketsort and keep track of what has been seen so far. I use a dictionary in order to keep constant time look up - opposed to appending to a list which exacerbates runtime. Each loop the dict is checked to see if the key exists, if it does then simply add to foundsum, otherwise set the dictionary for i to exist and add 2 times the "first occuring" digit to the expectedsum.

step: find first occuring numbers, create 2*sum then subtract expected sum from foundsum.

###[205. Isomorphic Strings ----(Easy)](https://leetcode.com/problems/isomorphic-strings/) 11:30 April 7, 2016

CSC330 exam tomorrow.. Sigh. 

This one took me a lot longer than it should've.... Misread their definition of isomorpic. Anyways, I use a hash table in order to map a character that has been seen to another character. The logic is as follows: if the char in s is not in the map and char in t is not a key, add the mapping for them. Otherwise, either a is a key or b is already mapped to. Then a simple constant time lookup can be done and see if they are equal, then we would have to map to a certain character twice.



###[226. Invert Binary Tree ---- (Easy)](https://leetcode.com/problems/invert-binary-tree/) 16:13 Monday, April 4 2016

Classic problem with a funny quote. Use top down tree recursion techniques to traverse. At each iteration of the "top" swap the left and right TreeNodes with classic swapping technique with a temp pointer. Try drawing out the steps on paper to visualize the recursion and swapping.


###[237. Delete a Node in a Linked List ---- (Easy)](https://leetcode.com/problems/delete-node-in-a-linked-list/) 16:13 Sunday, April 10 2016

This one is a test to know if you understand pointers in linked lists. Firstly, we can't just "remove" the specific node by saying node = null, as then we would lose the pointer to the next node. We also cant pick up that pointer because we have no reference to the previous pointer. With this in mind, we must instead make the specified's nodes value be equal to the next nodes value. Now, we can pick up the pointer by slapping on that node's next reference to the current node.next.
[1]->[0]->[....] becomes [0*]->[0&]->[...] and rearranging pointers results in [0*] -> [...].


###[292. Nim Game ---- (Easy)](https://leetcode.com/problems/nim-game/) 21:00 Sunday, April 3 2016
	

Simple answer... Why does this work? ( PLEASE DON'T TRY AND BRUTEFORCE!!!!!!!!!!)


First, write down the numbers 4, 5, 6, 7, 8, 9, 10 down. Observe at which positions you would lose at. 4 - no moves, 8 - no moves...etc. The name of the game is that IF the value is anything that is divisible by 4... no matter how many stones you remove (1,2,3), the opponent will always be able to count with 4 - <your move> in order to (inductively) make you reach the value 4. The converse is that YOU will be able to play the optimal move - always making the opponent's move be divisible by 4 and once again (inductively) forcing their move to be 4.