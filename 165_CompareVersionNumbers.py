class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        v1 = version1.split('.')
        v2 = version2.split('.')

        while v1 and v1[0] == '0':
            v1.pop(0)
        while v2 and v2[0] == '0':
            v2.pop(0)
            
        while v1 and v2:
            num1 = int(v1.pop(0))
            num2 = int(v2.pop(0))
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
        
        while v1 and int(v1[0]) == 0:
            v1.pop(0)
        while v2 and int(v2[0]) == 0:
            v2.pop(0)
            
        if v1:
            return 1
        elif v2:
            return -1
        else:
            return 0
