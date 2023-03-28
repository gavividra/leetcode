"""
6 - Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
"""

class Solution(object):
    def convert(self, s, numRows):
        ## Base Case:
        if(numRows == 1):
            return s
        output = ""
        for r in range(numRows):
            inc = 2*(numRows-1)
            for i in range(r, len(s), inc):
                output += s[i]
                if(r>0 and r<numRows-1 
                    and len(s) > i+inc-2*r):
                    output += s[i+inc-2*r]
        return output

        '''
        indent = numRows - 2
        space = ""
        for i in range(indent):
            space = space + " "
        output = ""
        string = s.split()
        for r in range(numRows):
            f = r
            while(f < len(string)):
                output += string[f] + space
                f = f + 2*(numRows-1)
            output = output + "\n"
        return output
        '''

        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
