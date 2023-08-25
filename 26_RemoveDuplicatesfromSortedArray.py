class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #V1
        result = 1
        array = []
        for i in range(1,len(nums),1):
            if nums[i-1] != nums[i]:
                nums[result] = nums[i]
                result +=1
        return result

        #V2
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
