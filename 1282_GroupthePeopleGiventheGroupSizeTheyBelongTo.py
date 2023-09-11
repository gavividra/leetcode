class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        groups = {}
        result = []
        
        for i, size in enumerate(groupSizes):
            if size not in groups:
                groups[size] = [i]
            else:
                groups[size].append(i)
            
            if len(groups[size]) == size:
                result.append(groups[size])
                groups[size] = []
        
        return result
