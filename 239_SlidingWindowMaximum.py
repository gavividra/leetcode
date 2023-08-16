class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #Time Limit Exceeded because it loops through every window
        result = []
        for i in range(0,len(nums)-k+1,1):
            max_num = nums[i]
            for j in range(i,k+i,1):
                if nums[j] > max_num:
                    max_num = nums[j]
            result.append(max_num)
        return result
