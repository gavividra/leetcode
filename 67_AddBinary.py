class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1 = list(a)  # Convert string to a list of characters
        a2 = list(b)  # Convert string to a list of characters
        length = max(len(a1), len(a2))

        # Make sure both lists have the same length by adding leading zeros
        while len(a1) < length:
            a1.insert(0, '0')
        while len(a2) < length:
            a2.insert(0, '0')

        carry = 0
        result = ''
        for i in range(length-1, -1, -1):
            carry += (1 if a1[i] == '1' else 0)
            carry += (1 if a2[i] == '1' else 0)
            result = ('1' if carry % 2 == 1 else '0') + result
            carry = (1 if carry >= 2 else 0)  # Change 1 to 2 to correctly handle carry
        if carry:
            result = '1' + result
        return result
