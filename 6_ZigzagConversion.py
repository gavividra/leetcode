class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        result = [""] * numRows
        index = 0
        step = 1 

        for char in s:
            result[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return "".join(result)

        '''
        # Version 2
        if numRows == 1 or numRows >= len(s):
            return s
        result = []
        index = 0
        step = 1 

        for char in s:
            if len(result) <= index:
                result.append(char)
            else:
                result[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return "".join(result)
        '''
        
