
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        
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
