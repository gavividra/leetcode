class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        string = str(num)
        check = True
        result = ""
        for i in string:
            if check and i=='6':
                check = False
                result += '9'
            else:
                result += i
        return int(result)
