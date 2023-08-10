class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0  # Initialize count of elements not equal to val
        left = 0   # Left pointer

        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]  
                left += 1
                count += 1
        return count
