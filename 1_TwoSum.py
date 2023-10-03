class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # # V1
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        
        # V2
        dict = {}
        for index, num in enumerate(nums):
          diff = target - num
          if(diff in dict):
            return [index, dict.get(diff)]
          dict[num] = index
