class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 1
        array = []
        for i in range(1,len(nums),1):
            if nums[i-1] != nums[i]:
                nums[result] = nums[i]
                result +=1
        return result
