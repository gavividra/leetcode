class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        # Version 1 -- needs to connect points 
        # (sometimes smallest distance forms 2 seperate figures)
        def calculate_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        result = 0
        history = []
        if len(points) <= 1:
            return 0
        for i in range(len(points)):
            min_distance = float('inf')
            current_point = points[i]
            point = i

            for j in range(len(points)):
                if i != j:
                    distance = calculate_distance(current_point, points[j])
                    if(distance<min_distance):
                        min_distance = min(min_distance, distance)
                        point = j

            print(str(current_point) + str(points[point]))
            if [i,point] not in history and [point,i] not in history:
                result += min_distance
                history.append([i,point])

        return result
