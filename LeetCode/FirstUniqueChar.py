from collections import OrderedDict
s = "loveleetcode"  
c = OrderedDict()
for ch in s:
    c[ch] = c.get(ch, 0) + 1
            
for k,v in c.iteritems():
    if v==1:
        print s.index(k) 
        break
print -1
