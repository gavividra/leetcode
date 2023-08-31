class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # # Trial 1
        # seen = ['A','A']
        # left = 1
        # string = ""
        # result = ""
        # for right, char in enumerate(s):
        #     if char != seen[right] and char != seen[right-left+2]:
        #         string = ""
        #         left = 1
        #     if char == seen[right]:
        #         left+=1
        #         string = seen[-1]
        #     if char == seen[right-left+2]:
        #         string = seen[right-left+2] + string + char
        #         left+=1
        #     if len(string) > len(result):
        #         result = string
        #     print(string)
        #     print(result)
        #     print("_____")
        #     seen.append(char)
        # return result

        # Version 2
        if len(s) <= 1:
            return s
        
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        longest = ""
        for i in range(len(s)):
            # For odd-length palindromes (centered at i)
            palindrome1 = expandAroundCenter(i, i)
            if len(palindrome1) > len(longest):
                longest = palindrome1
            
            # For even-length palindromes (centered at i and i+1)
            palindrome2 = expandAroundCenter(i, i + 1)
            if len(palindrome2) > len(longest):
                longest = palindrome2
        return longest

