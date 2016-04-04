# Coding_Challenges
Here's where I answer my (hopefully) daily Hackerrank, Leetcode, etc questions. Below I will write a quick explanation for each of my answers.











###[78. Subsets ----](https://leetcode.com/problems/subsets/) 8:00 Sunday, April 3 2016

	There are a couple ways to solve this. I use the fact that the sum of n choose i for i to n is equal to 2^n. This means that I can express each subset as a binary string where 1 means it is a part of the subset. Because converting an int (here is is value from 0 to 2^n) with bin() gives a binary string in the form 0b00001, I must slice the 0b and reverse it (although on second thought it will probably work if not reversed). This can be achieved usinng pythons list slicing tools [start:stop:step] with the step value on -1 and stop on 1. Next it is a matter of iterating the string and if the value is a 1, add it to the current subset. The rest is straight forward!