class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        max_num = 0
        for i in nums:
            if i>max_num:
                max_num = i
        for i in range(0,k,1):
            result = result + max_num + i
        return result
