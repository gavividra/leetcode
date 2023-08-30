class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Version 1
        counter = 0
        result = 0
        bank = []
        for i in s:
            if i in bank:
                result = max(counter,result)
                counter = 0
                bank = []
            else:
                counter += 1
                bank.append(i)
        return max(result,counter)
