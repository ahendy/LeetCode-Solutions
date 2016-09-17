from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = OrderedDict()
        self.cap = capacity
        

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.cache:
            return -1
            
        
        val = self.cache[key]
        del self.cache[key]
        self.cache[key] = val
        
        return val    

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        
        if key not in self.cache and len(self.cache)==self.cap:
            self.cache.popitem(last=False)
        
        elif key in self.cache:
            del self.cache[key]
        self.cache[key] = value
        
        
