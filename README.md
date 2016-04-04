# Coding_Challenges
Here's where I answer my (hopefully) daily Hackerrank, Leetcode, etc questions. Below I will write a quick explanation for each of my answers.







###[78. Subsets ----(Medium)](https://leetcode.com/problems/subsets/) 20:00 Sunday, April 3 2016

	
There are a couple ways to solve this. I use the fact that the sum of n choose i for i to n is equal to 2^n. This means that I can express each subset as a binary string where 1 means it is a part of the subset. Because converting an int (here is is value from 0 to 2^n) with bin() gives a binary string in the form 0b00001, I must slice the 0b and reverse it (although on second thought it will probably work if not reversed). This can be achieved using Python's list slicing tools [start:stop:step] with step value = -1 and stop = 1. Next it is a matter of iterating the string and if the value is a 1, add it to the current subset. The rest is straight forward!



###[292. Nim Game ---- (Easy)](https://leetcode.com/problems/nim-game/) 21:00 Sunda, April 3 2016
	

Simple answer... Why does this work? ( PLEASE DON'T TRY AND BRUTEFORCE!!!!!!!!!!)


First, write down the numbers 4, 5, 6, 7, 8, 9, 10 down. Observe at which positions you would lose at. 4 - no moves, 8 - no moves...etc. The name of the game is that IF the value is anything that is divisible by 4... no matter how many stones you remove (1,2,3), the opponent will always be able to count with 4 - <your move> in order to (inductively) make you reach the value 4. The converse is that YOU will be able to play the optimal move - always making the opponent's move be divisible by 4 and once again (inductively) forcing their move to be 4.