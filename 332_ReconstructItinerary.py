class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        
        '''
        # Version 1 -- Needs a while loop until tickets is empty
        airport = "JFK"
        result = []
        index = 0
        for ticket in tickets:
            if ticket[0] == airport:
                result.append(airport)
                airport = ticket[1]
                tickets.remove(ticket)
        return result
        '''

        '''
        # Version 2 -- Needs to find longest path
        def get_next_airport(airport):
            for i, ticket in enumerate(tickets):
                if ticket[0] == airport:
                    return i, ticket[1]
            return None, None

        result = []
        tickets.sort()
        airport = "JFK"

        while tickets:
            index, next_airport = get_next_airport(airport)
            if next_airport:
                result.append(airport)
                airport = next_airport
                del tickets[index]
            else:
                break

        result.append(airport)
        return result
        '''

        # Version 3 -- exceding time limit
        def get_next_airport(airport):
            for i, ticket in enumerate(tickets):
                if ticket[0] == airport:
                    return i, ticket[1]
            return None, None

        def dfs(airport):
            if len(result) == len(tickets) + 1:
                return True  # All tickets used
            index, next_airport = get_next_airport(airport)
            while next_airport:
                result.append(airport)
                if dfs(next_airport):
                    return True  # Found a valid path
                result.pop()  # Backtrack
                index, next_airport = get_next_airport(airport)
            return False

        result = []
        tickets.sort()
        airport = "JFK"

        dfs(airport)

        return result
