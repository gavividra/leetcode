class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hash_map = {}
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        
        list = []
        x = (len(nums)//3) + 1
        for num in hash_map:
            if hash_map[num] >= x:
                list.append(num)
        return list
