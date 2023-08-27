class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        '''
        V1
        check = -1
        for i in range(0,len(haystack)):
            if haystack[i] in needle[0]:
                check = i
                for j in range(0,len(needle)):
                    if haystack[i+j] != needle[j]:
                        check = -1
                if check != -1:
                    return check
        return -1
        '''
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
