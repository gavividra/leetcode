class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """       
        # Trial 1
        seen = ['A','A']
        left = 1
        string = ""
        result = ""
        for right, char in enumerate(s):
            if char != seen[right] and char != seen[right-left+2]:
                string = ""
                left = 1
            if char == seen[right]:
                left+=1
                string = seen[-1]
            if char == seen[right-left+2]:
                string = seen[right-left+2] + string + char
                left+=1
            if len(string) > len(result):
                result = string
            print(string)
            print(result)
            print("_____")
            seen.append(char)
        return result
