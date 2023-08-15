class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in range(1,len(nums)+1,1):
            if len(nums)%i == 0:
                result = result + nums[i-1]**2

        return result
