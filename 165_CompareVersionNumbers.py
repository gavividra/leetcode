class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        """
        #Version 1
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
        """  
        '''
        #Version 2
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        while v1 and v1[0] == '0':
            v1.pop(0)
        while v2 and v2[0] == '0':
            v2.pop(0)
            
        for i in range(len(v1)):
            num1 = int(v1[i])
            num2 = int(v2[i]) if i < len(v2) else 0
            
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
        
        if len(v2) > len(v1):
            for i in range(len(v1), len(v2)):
                if int(v2[i]) > 0:
                    return -1
        return 0
        ''' 

        '''
        #Version 3
        v1 = version1.split('.')
        v2 = version2.split('.')

        for i in range(0,min(len(v1),len(v2)),1):
            while v1[0] == '0':
                v1.pop(0)
            while v2[0] == '0':
                v2.pop(0)
            while len(v1[i]) < len(v2[i]):
                v1.append(0)
            while len(v1[i]) > len(v2[i]):
                v2.append(0)
            if int(v1[i]) > int(v2[i]):
                return 1
            if int(v1[i]) < int(v2[i]):
                return -1

        return 0
        '''

        #Version 4
        v1 = version1.split('.')
        v2 = version2.split('.')
        if(len(v1)>len(v2)):
            for i in range(0,len(v1)-len(v2)):
                v2.append('0')
        elif(len(v1)<len(v2)):
            for i in range(0,len(v2)-len(v1)):
                v1.append('0')
        result = 0
        for i in range(0,len(v1)):
            if(int(v1[i])<int(v2[i])):
                result = -1
                break
            elif(int(v1[i])>int(v2[i])):
                result =1
                break
        return result
