class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        '''
        # Version 1
        s_arr = []
        for i in s:
            if i.islower():
                s_arr.append(i)
            elif i.isupper():
                s_arr.append(i.lower())
        return s_arr[-1:] == s_arr[0:]
        '''

        # Version 2
        s_arr = []
        for i in s:
            if i.isalnum():
                s_arr.append(i.lower())
        return s_arr == s_arr[::-1]

        
