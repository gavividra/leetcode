class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        matrix = [[] for _ in range(numRows)]
        if numRows >= 1:
            matrix[0] = [1]
        if numRows >= 2:
            matrix[1] = [1,1]

        for i in range(2,numRows):
            matrix[i].append(1)
            for j in range(1,i):
                num = matrix[i-1][j-1] + matrix[i-1][j]
                matrix[i].append(num)
            matrix[i].append(1)            
        return matrix

