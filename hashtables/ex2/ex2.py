#  Hint:  You may not need all of these.  Remove the unused functions.

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    hashTable = {ticket.source: ticket.destination for ticket in tickets}
    route = [hashTable["NONE"]]
    for _ in range(length-1):
        route.append(hashTable[route[-1]])

    return route
