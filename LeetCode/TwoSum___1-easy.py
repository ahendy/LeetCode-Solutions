class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {} # key is value, value is indice
        for i in range(len(nums)):
            print map.get(target-nums[i])
            if(map.get(target-nums[i]) is not None):
                return [map.get(target-nums[i]), i]
            map.update( {nums[i]: i} )