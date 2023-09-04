class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        bank = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        result = 0
        prev = None
        for i in s[::-1]:
            if i == 'I' and (prev == 'V' or prev == 'X'):
                result -= 1
            elif i == 'X' and (prev == 'L' or prev == 'C'):
                result -= 10
            elif i == 'C' and (prev == 'D' or prev == 'M'):
                result -= 100            
            else:
                val = bank.get(i)
                result += val
            prev = i
        return result
