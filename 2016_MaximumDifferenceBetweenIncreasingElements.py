class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        diff = 0
        for i in range(0,len(nums)-1,1):
            for j in range(i,len(nums),1):
                if nums[j]-nums[i] > diff:
                    diff = nums[j]-nums[i]
        if diff ==0:
            return -1
        else:
            return diff
