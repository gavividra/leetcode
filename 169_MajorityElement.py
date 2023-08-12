class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        # Hard Version
        hash_map = {}
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        
        x = nums[0]
        for num in hash_map:
            if hash_map[num] > hash_map[x]:
                x = num
        return x
        '''

        #Easy Version
        nums.sort()
        return nums[(len(nums)-1)//2]

