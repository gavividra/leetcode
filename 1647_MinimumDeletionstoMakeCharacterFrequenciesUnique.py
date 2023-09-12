class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        my_dict = {}

        for char in s:
            if char not in my_dict:
                my_dict[char] = 1
            else:
                my_dict[char] += 1
        
        result = 0
        my_dict = sorted(my_dict.items(), key=lambda item: item[1], reverse=False)
        quantity = 0

        for char,value in my_dict:
            if value != quantity+1:
                result += abs(value-quantity)
        return result
        '''
