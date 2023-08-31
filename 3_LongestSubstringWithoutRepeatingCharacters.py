class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # # Version 1
        # counter = 0
        # result = 0
        # bank = []
        # for i in s:
        #     if i in bank:
        #         result = max(counter,result)
        #         counter = 0
        #         bank = []
        #     else:
        #         counter += 1
        #         bank.append(i)
        # return max(result,counter)

        # Version 2
        counter = 0
        result = 0
        bank = []
        for i in s:
            if i in bank:
                result = max(counter,result)
                counter = 0
                check = False
                for j in range(len(bank)-1,-1,-1):
                    if check==True or i == bank[j]:
                        bank.pop(j)
                        check = True
                    else:
                        counter += 1
            if i not in bank:
                counter += 1
                bank.append(i)
        return max(result,counter)

        # Version 3 - Taken from solutions
        seen = {}
        left = 0
        length = 0

        for right, char in enumerate(s):

            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            else:
                length = max(length, right - left + 1)
            
            seen[char] = right
        
        return length
