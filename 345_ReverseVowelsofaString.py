class Solution:
    def reverseVowels(self, s):
        v="aeiouAEIOU"
        s=list(s)
        l=0
        r=len(s)-1
        while l<r :
            if s[l] in v and s[r] in v :
                s[l],s[r]=s[r],s[l]
                l +=1 
                r -=1 
            elif s[l] not in v :
                l +=1 
            else :
                r -=1
        return ''.join(s)
'''                       
class Solution(object):
    def reverseVowels(self, s):
        v = "aeiouAEIOU"
        vowels = []
        characters = []
        word = ""
        z = 0
        for letter in s:
            if letter == a,e,i,o,u:
                vowels.insert(letter)
            characters.append(letter)
        for i in characters:
            if i == a,e,i,o,u:
                i = vowels[z]
                z += 1
        characters.join()
'''
