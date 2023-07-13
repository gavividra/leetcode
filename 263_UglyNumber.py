class Solution1(object):
    def isUgly(self, n):
        if n<1:
            return False
        while n%5 == 0:
            n = n/5
        while n%3 == 0:
            n = n/3
        while n%2 ==0:
            n = n/2
        return n==1
        """
        :type n: int
        :rtype: bool
        """

class Solution2(object):
    def isUgly(self, n):
        if n<1:
            return False
        for i in [2,3,5]:
            while n%i==0:
                n = n/i
        return n==1
        """
        :type n: int
        :rtype: bool
        """
