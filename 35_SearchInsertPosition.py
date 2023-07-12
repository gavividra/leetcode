class Solution(object):
    def searchInsert(self, nums, target):
        n = 0
        for i in nums:
            if i == target:
                return n
            if i > target:
                return n
            n = n+1
        return n
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
