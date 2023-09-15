class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        '''
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
        '''

        # Version 2
        def calculate_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        def find(parent, node):
            if parent[node] == node:
                return node
            parent[node] = find(parent, parent[node])
            return parent[node]

        def union(parent, rank, x, y):
            x_root = find(parent, x)
            y_root = find(parent, y)

            if x_root != y_root:
                if rank[x_root] < rank[y_root]:
                    parent[x_root] = y_root
                elif rank[x_root] > rank[y_root]:
                    parent[y_root] = x_root
                else:
                    parent[y_root] = x_root
                    rank[x_root] += 1

        result = 0
        n = len(points)
        edges = []

        # Create edges sorted by distance
        for i in range(n):
            for j in range(i + 1, n):
                dist = calculate_distance(points[i], points[j])
                edges.append((dist, i, j))

        edges.sort()  # Sort edges by distance

        parent = list(range(n))
        rank = [0] * n

        for edge in edges:
            dist, u, v = edge
            if find(parent, u) != find(parent, v):
                union(parent, rank, u, v)
                result += dist

        return result
