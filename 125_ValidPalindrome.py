class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_arr = []
        for i in s:
            if i.islower():
                s_arr.append(i)
            elif i.isupper():
                s_arr.append(i.lower())
        return s_arr[-1:] == s_arr[0:]
        
