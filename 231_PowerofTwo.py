class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #Mathmatical reasoning
        num = n
        if num <= 0:
            return False
        if num > 1:
            while num > 1:
                if num % 2 !=0:
                    return False
                num = num/2
            return True
        if num < 1:
            while num < 1:
                num = num*2
            if num != 1:
                return False
        return True

        '''
        #Using Bitwise (0010101 expressions for numbers)
        if n<=0:
            return False
        return (n&(n-1))==0
        '''
