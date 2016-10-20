class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        in_brack = []
        end = {
            ')':'(',
            '}':'{',
            ']': '[' 
        }
        
        for ch in s:
            
            if ch in end.values():
                in_brack.append(ch)
            
            if ch in end.keys():
                if len(in_brack) == 0 or end[ch] != in_brack.pop():
                    return False

        return len(in_brack) == 0 
        
