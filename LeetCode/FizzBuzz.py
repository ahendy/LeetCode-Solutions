class Solution(object):
    def fizzBuzz(self, n):
        return [(not i%3)*"Fizz" + (not i%5)*"Buzz" or str(i) for i in range(1, n+1)] 
