class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        cmpr = lambda x, y: -1 if x + y > y + x else 1 if x + y < y + x else 0
        nums = map(str, nums)
        nums = sorted(nums, cmp=cmpr)
        return str(int("".join(nums)))
        
