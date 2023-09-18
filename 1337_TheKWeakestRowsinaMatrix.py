class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        
        row_counts = [(i, sum(row)) for i, row in enumerate(mat)]
        
        row_counts.sort(key=lambda x: (x[1], x[0]))
        
        result = [x[0] for x in row_counts[:k]]
        
        return result
