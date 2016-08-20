ass Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        VOWELS = set(['a', 'e', 'i', 'o', 'u'])
        VOWELS |= set(map(lambda x: x.upper(), VOWELS))
        
        n = len(s)
        lo, hi = 0, n-1
        s = list(s)
       
        while lo < hi:
            if {s[lo], s[hi]} <= VOWELS: # is subset aka both in vowels
                s[lo], s[hi] = s[hi], s[lo] # python 1line swap
                lo += 1
                hi -= 1
                continue
            
            if s[lo] not in VOWELS:
                lo += 1
                
            if s[hi] not in VOWELS:
                hi -= 1
            
        return "".join(s)
