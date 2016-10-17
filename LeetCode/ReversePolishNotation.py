class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operator = {
            '+': lambda x,y : x+y
          , '-': lambda x,y : x-y
          , '/': lambda x,y : int(float(x)/y)
          , '*': lambda x,y : x*y
        }

        for token in tokens:
            if token in operator:
                if len(stack) >= 2:
                    f = stack.pop()
                    p = stack.pop()
                    eval = operator[token](p, f)
                    stack.append(eval)
                else:
                    return stack.pop()
            else:
                stack.append(int(token))

        return stack.pop()
                
            
