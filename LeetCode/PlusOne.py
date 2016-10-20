class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return []
    
        dig = list(reversed(digits))
        carry = 1
        
        for i, d in enumerate(dig):
            dig[i] = dig[i] + carry
            if dig[i] and dig[i] % 10 == 0:
                dig[i] = 0
                carry = 1
            else:
                carry = 0
                
            
        if carry:
            dig.append(carry)
                
        return list(reversed(dig))
            
            
        
