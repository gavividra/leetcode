class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        
        n = len(graph)
        endState = (1<<n)-1

        path_len = 0
        queue = collections.deque()
        visited = set()

        for i in range(n):
            queue.append((i, 1<<i))
        
        while queue:
            for i in range(len(queue)):
                node, curState = queue.popleft()

                if curState == endState:
                    return path_len

                if (node, curState) in visited:
                    continue
                
                visited.add((node, curState))
                for next_node in graph[node]:
                    queue.append((next_node, curState | 1<<next_node))
            path_len+=1
        
        return -1




                
